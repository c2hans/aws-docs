---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-mpts-modify-attributes-example.html
---

# Example
<a name="working-with-mpts-modify-attributes-example"></a>

This request changes the bitrate and video\_allocation of the MPTS with ID 3.

```
PUT http://198.51.100.0/mpts/3
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
----------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<mpts>
  <bitrate>30000000</bitrate>
  <video_allocation>25000000</video_allocation>
</mpts>
```
