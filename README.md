# Database model
```
class AirthimeticScheduling(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    load_type = models.CharField(max_length=64, db_column='load_type')
    start_date = models.BigIntegerField(db_column='start_date')
    end_date = models.BigIntegerField(db_column='end_date',blank = True)
    period_indicator = models.CharField(max_length=64, db_column='period_indicator', blank = True)
    period_interval = models.IntegerField(db_column='period_interval', blank=True)
    incremental_criteria = models.CharField(max_length=64, db_column='incremental_criteria',blank = True)
    incremental_criteria_type = models.CharField(max_length=64, db_column='incremental_criteria_type',blank = True)
    append = models.BooleanField(default = False,db_column='append')
    last_loaded_value = models.BigIntegerField(db_column='last_loaded_value',blank = True)
    last_run = models.BigIntegerField(db_column='last_run',blank=True)
    next_run = models.BigIntegerField(db_column='next_run',blank=True)
    status = models.CharField(max_length=64, db_column='status', blank=True)
    class Meta:
            # managed = False
        db_table = "airthmetic_job_details"

    def __str__(self):
        return str( self.id)
```