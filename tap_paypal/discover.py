"""Discover."""
# -*- coding: utf-8 -*-
from singer import metadata
from singer.catalog import Catalog, CatalogEntry

from tap_paypal.schema import load_schemas
from tap_paypal.streams import STREAMS

'''
def discover() -> Catalog:  # noqa: WPS210
    """Load the Stream catalog.

    Returns:
        Catalog -- The catalog
    """
    raw_schemas: dict = load_schemas()
    streams: list = []

    # Parse every schema
    for stream_id, schema in raw_schemas.items():

        stream_meta: dict = STREAMS[stream_id]
        # Create metadata
        mdata: list = metadata.get_standard_metadata(
            schema=schema.to_dict(),
            key_properties=stream_meta.get('key_properties', None),
            valid_replication_keys=stream_meta.get(
                'replication_keys',
                None,
            ),
            replication_method=stream_meta.get(
                'replication_method',
                None,
            ),
        )

        # Create a catalog entry
        streams.append(
            CatalogEntry(
                tap_stream_id=stream_id,
                stream=stream_id,
                schema=schema,
                key_properties=stream_meta.get('key_properties', None),
                metadata=mdata,
                replication_key=stream_meta.get(
                    'replication_key',
                    None,
                ),
                replication_method=stream_meta.get(
                    'replication_method',
                    None,
                ),
            ),
        )
    return Catalog(streams)
'''
#original discover function from singer tap template

def discover():
    raw_schemas = load_schemas()
    streams = []
    for stream_id, schema in raw_schemas.items():
        # TODO: populate any metadata and stream's key properties here..
        stream_metadata = []
        key_properties = []
        streams.append(
            CatalogEntry(
                tap_stream_id=stream_id,
                stream=stream_id,
                schema=schema,
                key_properties=key_properties,
                metadata=stream_metadata,
                replication_key=None,
                is_view=None,
                database=None,
                table=None,
                row_count=None,
                stream_alias=None,
                replication_method=None,
            )
        )
    return Catalog(streams)