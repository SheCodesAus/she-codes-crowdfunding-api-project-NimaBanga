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
   
    def create(self, validated_data):
        return Project.objects.create(**validated_data) #** indicate if data comes from dictionary it converst

class PledgeSerializer(serializers.ModelSerializer): #modelserializer command infer type of the fields from the model
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = [ 'id', 'supporter']
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)