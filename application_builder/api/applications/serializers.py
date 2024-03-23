from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.applications.models import (JobInfo, CandidateRequirements,
                                      RecruitRequirements, Application)
from apps.payments.models import Payment
from apps.applications import (EMPLOYMENT_TYPES, WORK_MODELS,
                               SCHEDULE_TYPES, CONTRACT_TYPES,
                               WORKING_CONDITIONS, EDUCATION_TYPES,
                               EXPERIENCES, DRIVING_SKILLS,
                               RECRUITER_RESPONSIBILITIES)
from .services import ApplicationService


User = get_user_model()


class ApplicationCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для валидации данных раздела общей информации."""
    class Meta:
        model = Application
        fields = (
            'title',
            'profession',
            'city',
            'min_salary',
            'max_salary',
            'number_of_employees',
            'start_working',
            'number_of_recruiters',
        )

    def update(self, instance, validated_data):
        service = ApplicationService(validated_data=validated_data)
        application = service.update_application(instance)
        return application


class JobInfoCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для валидации данных раздела условий труда."""
    employment_type = serializers.MultipleChoiceField(
        choices=EMPLOYMENT_TYPES,
        required=False
    )
    schedule = serializers.MultipleChoiceField(
        choices=SCHEDULE_TYPES,
        required=False
    )
    work_model = serializers.MultipleChoiceField(
        choices=WORK_MODELS,
        required=False)
    contract_type = serializers.MultipleChoiceField(
        choices=CONTRACT_TYPES,
        required=False
    )
    working_conditions = serializers.MultipleChoiceField(
        choices=WORKING_CONDITIONS,
        required=False
    )

    class Meta:
        model = JobInfo
        fields = (
            'employment_type',
            'schedule',
            'work_model',
            'contract_type',
            'working_conditions',
            'description'
        )

    def update(self, instance, validated_data):
        service = ApplicationService(validated_data=validated_data)
        job_info = service.update_job_info(instance)
        return job_info


class CandidateRequirementsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для валидации  данных раздела требований к соискателю."""
    education = serializers.MultipleChoiceField(
        choices=EDUCATION_TYPES,
        required=False
    )
    experience = serializers.MultipleChoiceField(
        choices=EXPERIENCES,
        required=False
    )
    driving_skills = serializers.MultipleChoiceField(
        choices=DRIVING_SKILLS,
        required=False
    )

    class Meta:
        model = CandidateRequirements
        fields = (
            'education',
            'experience',
            'language_skills',
            'driving_skills',
            'has_medical_certificate',
            'has_photo',
            'citizenship',
            'coreskills_and_responsibilities'
        )

    def update(self, instance, validated_data):
        service = ApplicationService(validated_data=validated_data)
        candidate_requirements = service.update_candidate_requirements(
            instance
        )
        return candidate_requirements


class RecruiterRequirementsCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания разделя требований к рекрутеру."""
    recruiter_responsibilities = serializers.MultipleChoiceField(
        choices=RECRUITER_RESPONSIBILITIES, required=False)

    class Meta:
        model = RecruitRequirements
        fields = (
            'industry',
            'english_skills',
            'recruiter_responsibilities',
            'description',
            'candidate_resume_form',
            'stop_list'
        )

    def update(self, instance, validated_data):
        service = ApplicationService(validated_data=validated_data)
        recruiter_requirements = service.update_recruiter_requirements(
            instance
        )
        return recruiter_requirements


class PaymentCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания способа оплаты."""
    class Meta:
        model = Payment
        fields = (
            'payment_amount',
            'payment_type'
        )

    def update(self, instance, validated_data):
        service = ApplicationService(validated_data=validated_data)
        payments = service.update_payments(instance)
        return payments


class FullApplicationCreateSerializer(serializers.Serializer):
    """Сериализатор для создания заявки."""
    application = ApplicationCreateSerializer()
    job_info = JobInfoCreateSerializer()
    candidate_requirements = CandidateRequirementsCreateSerializer()
    recruiter_requirements = RecruiterRequirementsCreateSerializer()
    payments = PaymentCreateSerializer()

    def save(self):
        current_user = self.context.get('request').user
        service = ApplicationService(validated_data=self.validated_data)
        application = service.save(current_user)
        return application


class JobInfoReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела условий труда."""

    class Meta:
        model = JobInfo
        fields = (
            'employment_type',
            'schedule',
            'work_model',
            'contract_type',
            'working_conditions',
            'description'
        )


class CandidateRequirementsReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела требований к кандидату."""
    language_skills = serializers.StringRelatedField(many=True)
    citizenship = serializers.StringRelatedField(many=True)

    class Meta:
        model = CandidateRequirements
        fields = (
            'education',
            'experience',
            'language_skills',
            'driving_skills',
            'has_medical_certificate',
            'has_photo',
            'citizenship',
            'coreskills_and_responsibilities'
        )


class RecruiterRequirementsReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения раздела требований к рекрутеру."""
    industry = serializers.StringRelatedField()

    class Meta:
        model = RecruitRequirements
        fields = (
            'industry',
            'english_skills',
            'recruiter_responsibilities',
            'description',
            'candidate_resume_form',
            'stop_list'
        )


class PaymentReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения способа оплаты."""
    class Meta:
        model = Payment
        fields = (
            'payment_amount',
            'payment_type'
        )


class FullApplicationReadSerializer(serializers.Serializer):
    """Сериализатор для чтения заяки целиком."""
    id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    title = serializers.CharField()
    city = serializers.StringRelatedField()
    profession = serializers.StringRelatedField()
    min_salary = serializers.IntegerField()
    max_salary = serializers.IntegerField()
    start_working = serializers.CharField()
    created_at = serializers.DateTimeField(format='%d:%m:%Y %H:%M')
    job_info = JobInfoReadSerializer()
    candidate_requirements = CandidateRequirementsReadSerializer()
    recruit_requirements = RecruiterRequirementsReadSerializer()
    payments = PaymentReadSerializer()
