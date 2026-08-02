---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-modify-spts-program-example.html
---

# Example
<a name="working-with-members-of-mpts-modify-spts-program-example"></a>

This example changes the MPTS member with the ID 6 in the MPTS that has the ID 2. The request changes one of the PID values.

```
PUT http://198.51.100.0/mpts/2/mpts_members/6
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_member>
  <pid_map>
    <pmt_pid>600</pmt_pid>
  </pid_map>
</mpts_member>
```
