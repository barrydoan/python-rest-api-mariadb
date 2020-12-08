from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Team, PlayerTeam
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']


class TeamSerialize(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_id', 'name', 'color']


class PlayerTeamSerialize(serializers.ModelSerializer):
    class Meta:
        model = PlayerTeam
        fields = ['player_id', 'first', 'last', 'percentage', 'teamName', 'color']