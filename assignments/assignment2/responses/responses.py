from marshmallow import Schema, fields

class DeepLinksInner(Schema):
    guid = fields.Str()
    bitlink = fields.Str()
    app_uri_path = fields.Str()
    install_url = fields.Str()
    app_guid = fields.Str()
    os = fields.Str()
    install_type = fields.Str()
    created = fields.Str()
    modified = fields.Str()
    brand_guid = fields.Str()

class RetrieveSchema(Schema):
    references = fields.Str()
    link = fields.Str()
    id = fields.Str()
    long_url = fields.Str()
    title = fields.Str()
    archived = fields.Boolean()
    created_at = fields.Str()
    created_by = fields.Str()
    client_id = fields.Str()
    custom_bitlinks = fields.Str()
    tags = fields.List(fields.Str())
    launchpad_ids = fields.List(fields.Str())
    deeplinks = fields.List(fields.Nested(DeepLinksInner))
