

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





# class EventPostUpdateSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = EventPost
# 		fields = ['title', 'body', 'image']

# 	def validate(self, blog_post):
# 		try:
# 			title = blog_post['title']
# 			if len(title) < MIN_TITLE_LENGTH:
# 				raise serializers.ValidationError({"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})
			
# 			body = blog_post['body']
# 			if len(body) < MIN_BODY_LENGTH:
# 				raise serializers.ValidationError({"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
			
# 			image = blog_post['image']
# 			url = os.path.join(settings.TEMP , str(image))
# 			storage = FileSystemStorage(location=url)

# 			with storage.open('', 'wb+') as destination:
# 				for chunk in image.chunks():
# 					destination.write(chunk)
# 				destination.close()

# 			# Check image size
# 			if not is_image_size_valid(url, IMAGE_SIZE_MAX_BYTES):
# 				os.remove(url)
# 				raise serializers.ValidationError({"response": "That image is too large. Images must be less than 2 MB. Try a different image."})

# 			# Check image aspect ratio
# 			if not is_image_aspect_ratio_valid(url):
# 				os.remove(url)
# 				raise serializers.ValidationError({"response": "Image height must not exceed image width. Try a different image."})

# 			os.remove(url)
# 		except KeyError:
# 			pass
# 		return blog_post


# class EventPostCreateSerializer(serializers.ModelSerializer):


# 	class Meta:
# 		model = EventPost
# 		fields = ['title', 'description', 'start_time', 'end_time', 'attendees', 'user', 'private']


# 	def save(self):
		
# 		try:
# 			title = self.validated_data['title']
# 			if len(title) < MIN_TITLE_LENGTH:
# 				raise serializers.ValidationError({"response": "Enter a title longer than " + str(MIN_TITLE_LENGTH) + " characters."})
			
# 			body = self.validated_data['description']
# 			if len(body) < MIN_BODY_LENGTH:
# 				raise serializers.ValidationError({"response": "Enter a body longer than " + str(MIN_BODY_LENGTH) + " characters."})
			
# 			event_post = EventPost(
# 								user=self.validated_data['user'],
# 								title=title,
# 								description=description,
#                                 start_time=self.validated_data['start_time'],
#                                 end_time=self.validated_data['end_time'],
#                                 attendees=self.validated_data['attendees'],
#                                 private=self.validated_data['private']
# 								)

# 			event_post.save()
# 			return event_post
# 		except KeyError:
# 			raise serializers.ValidationError({"response": "You must have a title, some content, and an start Time & End Time."})