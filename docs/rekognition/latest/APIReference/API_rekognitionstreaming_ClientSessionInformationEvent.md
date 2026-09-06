---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_ClientSessionInformationEvent.html
---

# ClientSessionInformationEvent
<a name="API_rekognitionstreaming_ClientSessionInformationEvent"></a>

Any information that the client needs to send for the streaming session. For face movement challenge, it will contain information like initial face position and target face position.

## Contents
<a name="API_rekognitionstreaming_ClientSessionInformationEvent_Contents"></a>

 ** Challenge **   <a name="rekognition-Type-rekognitionstreaming_ClientSessionInformationEvent-Challenge"></a>
Contains information on FaceMovementAndLightChellenge, TargetFace, and ColorDisplayed, for a given Challenge.
Type: [ClientChallenge](API_rekognitionstreaming_ClientChallenge.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_rekognitionstreaming_ClientSessionInformationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognitionstreaming-2022-05-30/ClientSessionInformationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognitionstreaming-2022-05-30/ClientSessionInformationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognitionstreaming-2022-05-30/ClientSessionInformationEvent)
