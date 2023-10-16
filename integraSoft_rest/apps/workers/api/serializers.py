from rest_framework import serializers

class WorkerHcmNamesSerializer(serializers.Serializer):
    legislation_code = serializers.CharField(source='LegislationCode',max_length=5)
    last_name = serializers.CharField(source='LastName',max_length=20)
    first_name = serializers.CharField(source='FirstName',max_length=20)
    middle_names = serializers.CharField(source='MiddleNames',max_length=20)
    display_name = serializers.CharField(source='DisplayName',max_length=20)
    order_name = serializers.CharField(source='OrderName',max_length=20)
    list_name = serializers.CharField(source='ListName',max_length=20)
    full_name = serializers.CharField(source='FullName',max_length=20)
    name_language = serializers.CharField(source='NameLanguage',max_length=20)
    created_by = serializers.CharField(source='CreatedBy',max_length=20)
    creation_date = serializers.CharField(source='CreationDate',max_length=20)
    last_updated_by = serializers.CharField(source='LastUpdatedBy',max_length=20)
    last_update_date = serializers.CharField(source='LastUpdateDate',max_length=20)
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link

class WorkerHcmEmailsSerializer(serializers.Serializer):
    email_address_id = serializers.CharField(source='EmailAddressId',max_length=30)
    email_type = serializers.CharField(source='EmailType',max_length=5)
    email_address = serializers.CharField(source='EmailAddress',max_length=20)
    from_date = serializers.CharField(source='FromDate',max_length=20)
    to_date = serializers.CharField(source='ToDate',max_length=20)
    created_by = serializers.CharField(source='CreatedBy',max_length=20)
    creation_date = serializers.CharField(source='CreationDate',max_length=20)
    last_updated_by = serializers.CharField(source='LastUpdatedBy',max_length=20)
    last_update_date = serializers.CharField(source='LastUpdateDate',max_length=20)
    primary_flag = serializers.CharField(source='PrimaryFlag',max_length=20)
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link

class WorkerHcmPhonesSerializer(serializers.Serializer):
    phone_id = serializers.CharField(source='PhoneId',max_length=20)
    phone_type = serializers.CharField(source='PhoneType',max_length=20)
    legislation_code = serializers.CharField(source='LegislationCode',max_length=20)
    country_code_number = serializers.CharField(source='CountryCodeNumber',max_length=20)
    phone_number = serializers.CharField(source='PhoneNumber',max_length=20)
    from_date = serializers.CharField(source='FromDate',max_length=20)
    created_by = serializers.CharField(source='CreatedBy',max_length=20)
    creation_date = serializers.CharField(source='CreationDate',max_length=20)
    last_updated_by = serializers.CharField(source='LastUpdatedBy',max_length=20)
    last_update_date = serializers.CharField(source='LastUpdateDate',max_length=20)
    primary_flag = serializers.CharField(source='PrimaryFlag',max_length=20)
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link

class WorkerHcmAddressesSerializer(serializers.Serializer):
    effective_start_date = serializers.CharField(source='EffectiveStartDate',max_length=20)
    effective_end_date = serializers.CharField(source='EffectiveEndDate',max_length=20)
    addressLine1 = serializers.CharField(source='AddressLine1',max_length=30)
    addressLine2 = serializers.CharField(source='AddressLine2',max_length=30)
    addressLine3 = serializers.CharField(source='AddressLine3',max_length=30)
    addressLine4 = serializers.CharField(source='AddressLine4',max_length=30)
    town_or_city = serializers.CharField(source='TownOrCity',max_length=30)
    region_1 = serializers.CharField(source='Region1',max_length=20)
    region_2 = serializers.CharField(source='Region2',max_length=20)
    region_3 = serializers.CharField(source='Region3',max_length=20)
    country = serializers.CharField(source='Country',max_length=20)
    postal_code = serializers.CharField(source='PostalCode',max_length=20)
    created_by = serializers.CharField(source='CreatedBy',max_length=50)
    creation_date = serializers.CharField(source='CreationDate',max_length=50)
    last_updated_by = serializers.CharField(source='LastUpdatedBy',max_length=20)
    last_update_date = serializers.CharField(source='LastUpdateDate',max_length=50)
    address_type = serializers.CharField(source='AddressType',max_length=20)
    primary_flag = serializers.CharField(source='PrimaryFlag',max_length=20)
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link    

class WorkRelationshipsAssignmentsSerializer(serializers.Serializer):
    assignment_id = serializers.CharField(source='AssignmentId',max_length=20)
    assignment_number = serializers.CharField(source='AssignmentNumber',max_length=20)
    assignment_name = serializers.CharField(source='AssignmentName',max_length=20)
    action_code = serializers.CharField(source='ActionCode',max_length=20)
    reason_code = serializers.CharField(source='ReasonCode',max_length=20)
    effective_start_date = serializers.CharField(source='EffectiveStartDate',max_length=20)
    effective_end_date = serializers.CharField(source='EffectiveEndDate',max_length=20)
    effective_sequence = serializers.CharField(source='EffectiveSequence',max_length=20)
    effective_latest_change = serializers.CharField(source='EffectiveLatestChange',max_length=20)
    business_unit_id = serializers.CharField(source='BusinessUnitId',max_length=20)
    business_unit_name = serializers.CharField(source='BusinessUnitName',max_length=20)
    assignment_type = serializers.CharField(source='AssignmentType',max_length=20)
    assignment_status_type_id = serializers.CharField(source='AssignmentStatusTypeId',max_length=20)
    assignment_status_type_code = serializers.CharField(source='AssignmentStatusTypeCode',max_length=20)
    assignment_status_type = serializers.CharField(source='AssignmentStatusType',max_length=20)
    system_person_type = serializers.CharField(source='SystemPersonType',max_length=20)
    user_person_type_id = serializers.CharField(source='UserPersonTypeId',max_length=20)
    user_person_type = serializers.CharField(source='UserPersonType',max_length=20)
    primary_flag = serializers.CharField(source='PrimaryFlag',max_length=20)
    primary_assignment_flag = serializers.CharField(source='PrimaryAssignmentFlag',max_length=20)
    synchronize_from_position_flag = serializers.CharField(source='SynchronizeFromPositionFlag',max_length=20)
    job_id = serializers.CharField(source='JobId',max_length=20)
    job_code = serializers.CharField(source='JobCode',max_length=20)
    department_id = serializers.CharField(source='DepartmentId',max_length=20)
    department_name = serializers.CharField(source='DepartmentName',max_length=20)
    location_id = serializers.CharField(source='LocationId',max_length=20)
    location_code = serializers.CharField(source='LocationCode',max_length=20)
    work_at_home_flag = serializers.CharField(source='WorkAtHomeFlag',max_length=20)
    assignment_category = serializers.CharField(source='AssignmentCategory',max_length=20)
    worker_category = serializers.CharField(source='WorkerCategory',max_length=20)
    permanent_temporary = serializers.CharField(source='PermanentTemporary',max_length=20)
    full_part_time = serializers.CharField(source='FullPartTime',max_length=20)
    manager_flag = serializers.CharField(source='ManagerFlag',max_length=20)
    hourly_salaried_code = serializers.CharField(source='HourlySalariedCode',max_length=20)
    normal_hours = serializers.CharField(source='NormalHours',max_length=20)
    frequency = serializers.CharField(source='Frequency',max_length=20)
    labour_union_member_flag = serializers.CharField(source='LabourUnionMemberFlag',max_length=20)
    union_id = serializers.CharField(source='UnionId',max_length=20)
    union_name = serializers.CharField(source='UnionName',max_length=20)
    collective_agreement_id = serializers.CharField(source='CollectiveAgreementId',max_length=20)
    collective_agreement_name = serializers.CharField(source='CollectiveAgreementName',max_length=20)
    standard_working_hours = serializers.CharField(source='StandardWorkingHours',max_length=20)
    standard_frequency = serializers.CharField(source='StandardFrequency',max_length=20)
    created_by = serializers.CharField(source='CreatedBy',max_length=20)
    creation_date = serializers.CharField(source='CreationDate',max_length=20)
    last_updated_by = serializers.CharField(source='LastUpdatedBy',max_length=20)
    last_update_date = serializers.CharField(source='LastUpdateDate',max_length=20)
    link = serializers.SerializerMethodField()

    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link    

class WorkerHcmWorkRelationshipsSerializer(serializers.Serializer):
    period_of_service_id = serializers.CharField(source='PeriodOfServiceId',max_length=20)
    legislation_code = serializers.CharField(source='LegislationCode',max_length=20)
    legal_entity_id = serializers.CharField(source='LegalEntityId',max_length=20)
    legal_employer_name = serializers.CharField(source='LegalEmployerName',max_length=20)
    worker_type = serializers.CharField(source='WorkerType',max_length=20)
    primary_flag = serializers.CharField(source='PrimaryFlag',max_length=20)
    start_date = serializers.CharField(source='StartDate',max_length=20)
    legal_employer_seniority_date = serializers.CharField(source='LegalEmployerSeniorityDate',max_length=20)
    enterprise_seniority_date = serializers.CharField(source='EnterpriseSeniorityDate',max_length=20)
    on_military_service_flag = serializers.CharField(source='OnMilitaryServiceFlag',max_length=20)
    worker_number = serializers.CharField(source='WorkerNumber',max_length=20)
    recommended_for_rehire = serializers.CharField(source='RecommendedForRehire',max_length=20)
    recommendation_reason = serializers.CharField(source='RecommendationReason',max_length=20)
    recommendation_authorized_by_person_id = serializers.CharField(source='RecommendationAuthorizedByPersonId',max_length=20)
    created_by = serializers.CharField(source='CreatedBy',max_length=20)
    creation_date = serializers.CharField(source='CreationDate',max_length=20)
    last_updated_by = serializers.CharField(source='LastUpdatedBy',max_length=20)
    last_update_date = serializers.CharField(source='LastUpdateDate',max_length=20)
    projected_termination_date = serializers.CharField(source='ProjectedTerminationDate',max_length=20)
    link = serializers.SerializerMethodField()
    assignments = WorkRelationshipsAssignmentsSerializer(many=True)

    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link

class WorkerHcmSerializer(serializers.Serializer):
    person_id = serializers.CharField(max_length=20, read_only=True)
    person_number = serializers.CharField(max_length=20, read_only=True)
    date_of_birth = serializers.CharField(max_length=20)
    date_of_death = serializers.CharField(max_length=20)
    country_of_birth = serializers.CharField(max_length=20)
    region_of_birth = serializers.CharField(max_length=20)
    town_of_birth = serializers.CharField(max_length=20)
    created_by = serializers.CharField(max_length=20)
    creation_date = serializers.CharField(max_length=20)
    last_updated_by = serializers.CharField(max_length=20,read_only=True)
    last_update_date = serializers.CharField(max_length=20, read_only=True)
    link = serializers.SerializerMethodField()
    names = WorkerHcmNamesSerializer(many=True)
    emails = WorkerHcmEmailsSerializer(many=True)
    phones = WorkerHcmPhonesSerializer(many=True)
    addresses = WorkerHcmAddressesSerializer(many=True)
    work_relationships = WorkerHcmWorkRelationshipsSerializer(many=True)
    
    def get_link(self, obj):
        first_link = obj.get('links')[0].get('href')
        return first_link


# PeopleSoft

class WorkerPeopleSoftSerializer(serializers.Serializer):
    emplid = serializers.CharField(source='EMPLID',max_length=20)
    name = serializers.CharField(source='NAME',max_length=20)
    descr = serializers.CharField(source='DESCR',max_length=20)
    price = serializers.CharField(source='PRICE',max_length=20)
    stock = serializers.CharField(source='STOCK',max_length=20)
    link = serializers.SerializerMethodField()