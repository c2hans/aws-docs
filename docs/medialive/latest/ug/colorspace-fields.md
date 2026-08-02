---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/colorspace-fields.html
---

# Reference: Location of fields
<a name="colorspace-fields"></a>

Read this section if you know how to handle color space in MediaLive, and you only need a reminder of where the fields are located in the MediaLive Console.

<table>
<thead>
  <tr><th>Topic</th><th colspan="2">Location on the Channel page</th><th>Field</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2">Input handling</td><td rowspan="2">Input attachments</td><td rowspan="2">Video Selector</td><td>Color space</td></tr>
  <tr><td>Color space usage</td></tr>
  <tr><td rowspan="2">Enter the display metadata for an input from a AWS Elemental Link device</td><td rowspan="2">Input attachments</td><td rowspan="2">Video Selector, then Color space settings</td><td>Max CLL</td></tr>
  <tr><td>Max Fall</td></tr>
  <tr><td rowspan="4">Output, configure the video codec</td><td rowspan="4">Output groups, then Outputs</td><td>Stream settings, then Video </td><td>Codec settings</td></tr>
  <tr><td rowspan="3">Stream settings, then Video, then Codec settings, then Codec details</td><td>Profile</td></tr>
  <tr><td>Tier</td></tr>
  <tr><td>Level</td></tr>
  <tr><td>Output, convert the color space</td><td>Output groups, then Outputs</td><td>Stream settings, then Video, then Color space</td><td> Color space settings</td></tr>
  <tr><td>Output, include or omit color space metadata</td><td>Output groups, then Outputs</td><td>Stream settings, then Video, then Codec settings, then Codec details, then Additional settings</td><td>Color metadata</td></tr>
  <tr><td rowspan="2">Output, specify display metadata to include, only if you are converting to HDR10</td><td rowspan="2">Output groups, then Outputs</td><td rowspan="2">Stream settings, then Video, then Color space, then Color space settings</td><td>Max CLL</td></tr>
  <tr><td>Max Fall</td></tr>
  <tr><td rowspan="2">Output, set up enhanced VQ, only if the output codec is H.264</td><td rowspan="2">Output groups, then Outputs</td><td rowspan="2">Stream settings, then Video, then Codec settings, then Additional encoding settings</td><td>Quality level</td></tr>
  <tr><td>Filter settings</td></tr>
</tbody>
</table>
