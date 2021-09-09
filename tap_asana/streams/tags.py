import datetime

from tap_asana.context import Context
from tap_asana.streams.base import Stream


class Tags(Stream):
  name = 'tags'
  replication_method = 'FULL_TABLE'
  fields = [
    "gid",
    "resource_type",
    "created_at",
    "followers",
    "name",
    "color",
    "notes",
    "permalink_url",
    "workspace"
  ]  


  def get_objects(self):
    opt_fields = ",".join(self.fields)
    for workspace in self.call_api("workspaces"):
      for tag in self.call_api("tags", workspace=workspace["gid"], opt_fields=opt_fields):
        yield tag


Context.stream_objects['tags'] = Tags
