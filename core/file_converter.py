import core.exporter_thread
import os
import shutil
from core.tag_converter import TagConverter
from widget.export_mapper_widget import ExportMapperWidget

class FileConverter:
   def __init__(self, in_file:str, process_opt:str, out_file:str, export_mapper:ExportMapperWidget):
      self._infile = in_file
      self._outfile = out_file
      self._processOption = process_opt
      self._exportMapper = export_mapper
      
   @property
   def input_file(self):
      return self._infile
   
   @property
   def output_file(self):
      return self._outfile
   
   @property
   def process_option(self):
      return self._processOption

   @property
   def export_mapper(self):
      return self._exportMapper
   
   def convert(self, thread:core.exporter_thread.ExporterThread):
      if self._processOption == 'Ignore':
         pass
      elif self._processOption == 'Copy Over':
         if os.path.isdir(self._infile):
            if not os.path.exists(self._outfile):
               os.makedirs(self._outfile)
         elif os.path.isfile(self._infile):
            directory = os.path.dirname(self._outfile)
            if not os.path.exists(directory):
               os.makedirs(directory)
            shutil.copyfile(self._infile, self._outfile)
      elif self._processOption == 'BSS to Django':         
         tag_converter = TagConverter(self.input_file, self.export_mapper, thread)
         
         with open(self.output_file, 'w') as output_file:
            output_file.write(tag_converter.convert())
         
         
      