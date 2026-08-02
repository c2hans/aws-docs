---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-get-list-mpts-output-statuses-example.html
---

# Example
<a name="working-with-mpts-get-list-mpts-output-statuses-example"></a>

This request returns information for the two MPTS outputs that exist in the cluster.

```
GET http://198.51.100.0/mpts/statuses
--------------------------------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_statuses href="/mpts/statuses" product="AWS Elemental Conductor Live version="3.3.nnnnn">
  <mpts_status>
    <id type="integer">1</id>
    <status>running</status>
  </mpts_status>
  <mpts_status>
    <id type="integer">4</id>
    <status>running</status>
  </mpts_status>
</mpts_statuses>
```
