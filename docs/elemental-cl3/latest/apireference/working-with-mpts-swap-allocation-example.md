---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-swap-allocation-example.html
---

# Example
<a name="working-with-mpts-swap-allocation-example"></a>

This request swaps the allocation\_message\_priority values of the MPTS with ID 3 and the MPTS with the ID 4.

```
PUT http://198.51.100.0/mpts/swap_allocation_priority
----------------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
----------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts_ids>
  <mpts_id>1</mpts_id>
  <mpts_id>3</mpts_id>
</mpts_ids>
```
