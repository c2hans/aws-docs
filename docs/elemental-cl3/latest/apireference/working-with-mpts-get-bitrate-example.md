---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-bitrate-example.html
---

# Example
<a name="working-with-mpts-get-bitrate-example"></a>

This request returns the statistics for the MPTS with the ID 5. This MPTS contains two MPTS members (IDs 30 and 29).

```
GET http://198.51.100.0/mpts/5/stats
--------------------------------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_stats>
  <id type="integer">10</id>
  <mpts_members type="array">
    <mpts_member>
      <id type="integer">30</id>
      <name>Channel_C</name>
      <series_data type="array">
        <series_datum>
          <timestamp type="integer">1418939884</timestamp>
          <mpts_id type="integer">10</mpts_id>
          <channel_id type="integer">8</channel_id>
          <bitrate type="float">0</bitrate>
        </series_datum>
        <series_datum>
          <timestamp type="integer">1418939886</timestamp>
          <mpts_id type="integer">5</mpts_id>
          <channel_id type="integer">8</channel_id>
          <bitrate type="float">7045000.0</bitrate>
        </series_datum>
        <series_datum>
.
.
.
        </series_datum>
      </series_data>
    </mpts_member>
    <mpts_member>
      <id type="integer">29</id>
      <name>Channel_F</name>
      <series_data type="array">
        <series_datum>
          <timestamp type="integer">1418939884</timestamp>
        <series_datum>
.
.
.
        </series_datum>
      </series_data>
    </mpts_member>
  </mpts_members>
</mpts_stats>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
