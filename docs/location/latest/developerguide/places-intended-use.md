---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/places-intended-use.html
---

# IntendedUse
<a name="places-intended-use"></a>

**Note**
If results are stored, then they will be billed at the higher storage pricing tier. Use request parameter `IntendedUse` to specify whether the results are for single use or storage. See [Places pricing](places-pricing.md) to understand costs associated with stored results.

When you call a place API, specify `IntendedUse` by setting the value to be either `SingleUse` or `Storage`, based on the intended use of the results. If you are going to store the results (even for caching purposes), you must choose the *storage* option, not the *single use* option.

| Filter Type | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SingleUse | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Storage | Yes | Yes | No | Yes | Yes | Yes | No |
