from rest_framework import serializers
from .models import Project, Pledge

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField(read_only=True) #since we said in models the date time of creation will be automatically populated, user should not eb able to edit it.
    owner = serializers.ReadOnlyField(source='owner.id')
    project_date = serializers.DateField() #NB
    project_starttime = serializers.DateTimeField() #NB
    project_endtime = serializers.DateTimeField() #NB
    project_location = serializers.CharField(max_length=200)

   
    def create(self, validated_data):
        return Project.objects.create(**validated_data) #** indicate if data comes from dictionary it converst

class PledgeSerializer(serializers.ModelSerializer): #modelserializer command infer type of the fields from the model
    class Meta:
        model = Pledge
        fields = ['id', 'pledge_time', 'comment', 'project', 'supporter', 'pledge_date']
        read_only_fields = [ 'id', 'project','supporter','pledge_date']
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title) #The last part indicates that if we dont get a title use the current instance's title
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        # instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.project_date = validated_data.get('project_date', instance.project_date) #NB1
        instance.project_starttime = validated_data.get('project_starttime', instance.project_starttime) #NB
        instance.project_endtime = validated_data.get('project_endtime', instance.project_endtime) #NB
        instance.project_location = validated_data.get('project_location', instance.project_location) #NB
        instance.save()
        return instance

