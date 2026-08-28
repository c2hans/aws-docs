---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.OtherParms.html
---

# Other parameters that affect autovacuum
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum.OtherParms"></a>

The following query shows the values of some of the parameters that directly affect autovacuum and its behavior. The [autovacuum parameters](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html) are described fully in the PostgreSQL documentation.

```
SELECT name, setting, unit, short_desc
FROM pg_settings
WHERE name IN (
'autovacuum_max_workers',
'autovacuum_analyze_scale_factor',
'autovacuum_naptime',
'autovacuum_analyze_threshold',
'autovacuum_analyze_scale_factor',
'autovacuum_vacuum_threshold',
'autovacuum_vacuum_scale_factor',
'autovacuum_vacuum_threshold',
'autovacuum_vacuum_cost_delay',
'autovacuum_vacuum_cost_limit',
'vacuum_cost_limit',
'autovacuum_freeze_max_age',
'maintenance_work_mem',
'vacuum_freeze_min_age');
```

While these all affect autovacuum, some of the most important ones are:
+ [maintenance\_work\_mem](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#GUC-MAINTENANCE_WORK_MEM)
+ [autovacuum\_freeze\_max\_age](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE)
+ [autovacuum\_max\_workers](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MAX-WORKERS)
+ [autovacuum\_vacuum\_cost\_delay](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-DELAY)
+ [ autovacuum\_vacuum\_cost\_limit](https://www.postgresql.org/docs/current/static/runtime-config-autovacuum.html#GUC-AUTOVACUUM-VACUUM-COST-LIMIT)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
