---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeletePrefetchSchedule.html
---

# DeletePrefetchSchedule
<a name="API_DeletePrefetchSchedule"></a>

Deletes a prefetch schedule for a specific playback configuration. If you call `DeletePrefetchSchedule` on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. For more information about ad prefetching, see [Using ad prefetching](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html) in the *MediaTailor User Guide*.

## Request Syntax
<a name="API_DeletePrefetchSchedule_RequestSyntax"></a>

```
DELETE /prefetchSchedule/{{PlaybackConfigurationName}}/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePrefetchSchedule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_DeletePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-DeletePrefetchSchedule-request-uri-Name"></a>
The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.
Required: Yes

 ** [PlaybackConfigurationName](#API_DeletePrefetchSchedule_RequestSyntax) **   <a name="mediatailor-DeletePrefetchSchedule-request-uri-PlaybackConfigurationName"></a>
The name of the playback configuration for this prefetch schedule.
Required: Yes

## Request Body
<a name="API_DeletePrefetchSchedule_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePrefetchSchedule_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeletePrefetchSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeletePrefetchSchedule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeletePrefetchSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DeletePrefetchSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DeletePrefetchSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
