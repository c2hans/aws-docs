---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetSessionIdentifier.html
---

# BatchGetSessionIdentifier
<a name="API_BatchGetSessionIdentifier"></a>

The identifiers for a session.

## Contents
<a name="API_BatchGetSessionIdentifier_Contents"></a>

 ** farmId **   <a name="deadlinecloud-Type-BatchGetSessionIdentifier-farmId"></a>
The farm ID of the session.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetSessionIdentifier-jobId"></a>
The job ID of the session.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetSessionIdentifier-queueId"></a>
The queue ID of the session.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** sessionId **   <a name="deadlinecloud-Type-BatchGetSessionIdentifier-sessionId"></a>
The session ID.
Type: String
Pattern: `session-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_BatchGetSessionIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetSessionIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetSessionIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetSessionIdentifier)
