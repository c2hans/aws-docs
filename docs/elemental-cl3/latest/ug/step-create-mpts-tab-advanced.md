---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/step-create-mpts-tab-advanced.html
---

# Advanced tab – Suppressing generation of SI/PSI tables
<a name="step-create-mpts-tab-advanced"></a>

Many of the fields on this tab let you control generation of all the SI/PSI tables that Elemental Statmux can generate. For guidance for disabling generation of these tables, see [Passing through SI/PSI tables](mpts-passthrough-PSI-pids.md).

| Field | Description |
| --- | --- |
| Suppress PMT Generation | Check this field if you don't want Elemental Statmux to generate PMTs for any of the programs in the MPTS. For a standard MPTS, you leave this field unchecked.  |
| PAT Interval | If you want Elemental Statmux to generate this table for the MPTS, check the field and set the interval. For a standard MPTS, you check this field. |
| SDT Interval | If you want Elemental Statmux to generate this table for the MPTS, check the field and set the interval. Elemental Statmux creates the SDT table. For a standard MPTS, you check this field.<br />For each program in the MPTS, Elemental Statmux creates the SDT information as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/ug/step-create-mpts-tab-advanced.html) |
| TDT Interval | If you want Elemental Statmux to generate this table for the MPTS, check the field and set the interval. For a standard MPTS, this field is optional. |
| Enable NIT Information Table (NIT) | If you want Elemental Statmux to generate this table for the MPTS, check the field and complete the data fields. For a standard MPTS, this field is optional. |
