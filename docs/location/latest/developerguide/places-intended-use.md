---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/places-intended-use.html
---

# IntendedUse
<a name="places-intended-use"></a>

**Note**
If you store results, the higher storage pricing tier applies. Use the request parameter `IntendedUse` to specify whether the results are for single use or storage. For more information about costs associated with stored results, see [Places pricing](places-pricing.md).

When you call a place API, specify `IntendedUse` by setting the value to be either `SingleUse` or `Storage`, based on the intended use of the results. If you are going to store the results (even for caching purposes), you must choose the *storage* option, not the *single use* option.

| Filter Type | Geocode | Reverse Geocode | Autocomplete | Get Place | Search Text | Search Nearby | Suggest |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SingleUse | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Storage | Yes | Yes | No | Yes | Yes | Yes | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
