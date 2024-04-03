"""Serializers for the SearchResult model."""

from rest_framework import serializers

from api_v2 import models
from api import models as v1

class SearchResultSerializer(serializers.ModelSerializer):
    object = serializers.SerializerMethodField(method_name='get_object')
    document = serializers.SerializerMethodField(method_name='get_document')


    class Meta:
        model = models.SearchResult
        fields = [
            'document',
            'object_pk',
            'object_name',
            'object',
            'object_model',
            'schema_version',
            'rank',
            'text',
            'highlighted']

    def get_object(self, obj):
        if obj.schema_version == 'v1':
            if obj.object_model == 'MagicItem':
                result_detail = v1.MagicItem.objects.get(slug=obj.object_pk)
                return result_detail.search_result_extra_fields()
                
            if obj.object_model == 'Monster':
                result_detail = v1.Monster.objects.get(slug=obj.object_pk)
                return result_detail.search_result_extra_fields()
                
            if obj.object_model == 'Spell':
                result_detail = v1.Spell.objects.get(slug=obj.object_pk)
                return result_detail.search_result_extra_fields()

            if obj.object_model == 'Section':
                result_detail = v1.Section.objects.get(slug=obj.object_pk)
                return result_detail.search_result_extra_fields()

    def get_document(self, obj):
        if obj.schema_version == 'v1':
            doc = v1.Document.objects.get(slug=obj.document_pk)
            return {
                'key': doc.slug,
                'name': doc.title
                }

        if obj.schema_version == 'v2':
            doc = models.Document.objects.get(key=obj.document_pk)
            return {
                'key': doc.key,
                'name': doc.name
                }