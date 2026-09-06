---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_ParticipatingResource.html
---

# ParticipatingResource
<a name="API_ParticipatingResource"></a>

Represents a resource participating in an asynchronous Job.

## Contents
<a name="API_ParticipatingResource_Contents"></a>

 ** launchStatus **   <a name="drs-Type-ParticipatingResource-launchStatus"></a>
The launch status of a participating resource.
Type: String
Valid Values: `PENDING | IN_PROGRESS | LAUNCHED | FAILED | TERMINATED`
Required: No

 ** participatingResourceID **   <a name="drs-Type-ParticipatingResource-participatingResourceID"></a>
The ID of a participating resource.
Type: [ParticipatingResourceID](API_ParticipatingResourceID.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_ParticipatingResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/ParticipatingResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/ParticipatingResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/ParticipatingResource)
