---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/origin-query-parameters.html
---

# MediaTailor query parameter handling for origins
<a name="origin-query-parameters"></a>

AWS Elemental MediaTailor handles query parameters differently depending on their purpose. Manifest query parameters (prefixed with `manifest.`) are used for CDN routing and authorization, while other query parameters can be used for origin-specific functionality.

**Time-shifted viewing with MediaPackage**
For time-shifted viewing functionality with MediaPackage, you can include `start` and `end` parameters in your requests. These parameters define specific content windows for startover and catch-up viewing.

**Example time-shifted viewing request**
Include start and end parameters in your manifest request for time-shifted viewing:

```
GET /v1/master/{{111122223333}}/{{originId}}/index.m3u8?start=2024-08-26T10:00:00Z&end=2024-08-26T11:00:00Z
```

**Parameter behavior during sessions**
Query parameters are processed at session initialization. For time-shifted viewing or other origin-specific features:
+ **Session initialization:** Include required parameters with the initial manifest request
+ **Parameter persistence:** Parameters are associated with the session and maintained throughout playback
+ **Changing parameters:** To modify time-shift windows or other parameters, create a new session with updated values

**Important**
The specific handling of query parameters depends on your origin configuration and the parameters your content origin supports. For MediaPackage integration, ensure your CDN is configured to forward the necessary query parameters as described in [Configure essential query parameters](mediapackage-integration.md#mediapackage-query-strings).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
