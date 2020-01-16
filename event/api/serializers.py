

from rest_framework import serializers
import os
from event.models import EventPost
import dateparser

MIN_TITLE_LENGTH = 5
MIN_BODY_LENGTH = 50


class EventPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = ['title', 'description', 'start_time', 'end_time', 'attendees', 'private']

    def is_valid(self, event_post):
        try:
            title = event_post['title']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError({"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})

            description = event_post['description']
            if len(description) < MIN_BODY_LENGTH:
                raise serializers.ValidationError({"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
        
        except KeyError:
            pass
        try:
            start_time = dateparser.parse(event_post['start_time'])
        except:
            raise serializers.ValidationError({"response": "Start Time must be in format YYYY-MM-DD HH:MM"})

        try:
            end_time = dateparser.parse(event_post['end_time'])
        except:
            raise serializers.ValidationError({"response": "End Time must be in format DD/MM/YYYY HH:MM"})

        try:
            attendees = int(event_post['attendees'])
        except:
            raise serializers.ValidationError({"response": "Attenedees must be a integer"})

        
        try:
            private = event_post['private']
        except:
            private = False
        return event_post


    def save(self, event_post):
        try:
            title = event_post['title']
            if len(title) < MIN_TITLE_LENGTH:
                raise serializers.ValidationError({"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})

            description = event_post['description']
            if len(description) < MIN_BODY_LENGTH:
                raise serializers.ValidationError({"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
        
        except KeyError:
            pass
        try:
            start_time = event_post['start_time']
        except:
            raise serializers.ValidationError({"response": "Start Time must be in format DD/MM/YYYY HH:MM"})

        try:
            end_time = event_post['end_time']
        except:
            raise serializers.ValidationError({"response": "End Time must be in format DD/MM/YYYY HH:MM"})

        try:
            attendees = int(event_post['attendees'])
        except:
            raise serializers.ValidationError({"response": "Attenedees must be a integer"})

        try:
            private = bool(event_post['private'])
        except:
            private = False

        event_post = EventPost(
                            title=title,
                            description=description,
                            start_time=start_time,
                            end_time=end_time,
                            attendees=attendees,
                            private=private
                            )
        event_post.save()
        
        return event_post
        





class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPost
        fields = ['title', 'description', 'start_time', 'end_time', 'attendees', 'private', 'slug']




