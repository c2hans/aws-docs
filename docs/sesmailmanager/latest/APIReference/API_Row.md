---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_Row.html
---

# Row
<a name="API_Row"></a>

A result row containing metadata for an archived email message.

## Contents
<a name="API_Row_Contents"></a>

 ** ArchivedMessageId **   <a name="sesmailmanager-Type-Row-ArchivedMessageId"></a>
The unique identifier of the archived message.
Type: String
Required: No

 ** Cc **   <a name="sesmailmanager-Type-Row-Cc"></a>
The email addresses in the CC header.
Type: String
Required: No

 ** Date **   <a name="sesmailmanager-Type-Row-Date"></a>
The date the email was sent.
Type: String
Required: No

 ** Envelope **   <a name="sesmailmanager-Type-Row-Envelope"></a>
The SMTP envelope information of the email.
Type: [Envelope](API_Envelope.md) object
Required: No

 ** From **   <a name="sesmailmanager-Type-Row-From"></a>
The email address of the sender.
Type: String
Required: No

 ** HasAttachments **   <a name="sesmailmanager-Type-Row-HasAttachments"></a>
A flag indicating if the email has attachments.
Type: Boolean
Required: No

 ** IngressPointId **   <a name="sesmailmanager-Type-Row-IngressPointId"></a>
The ID of the ingress endpoint through which the email was received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** InReplyTo **   <a name="sesmailmanager-Type-Row-InReplyTo"></a>
The email message ID this is a reply to.
Type: String
Required: No

 ** MessageId **   <a name="sesmailmanager-Type-Row-MessageId"></a>
The unique message ID of the email.
Type: String
Required: No

 ** ReceivedHeaders **   <a name="sesmailmanager-Type-Row-ReceivedHeaders"></a>
The received headers from the email delivery path.
Type: Array of strings
Required: No

 ** ReceivedTimestamp **   <a name="sesmailmanager-Type-Row-ReceivedTimestamp"></a>
The timestamp of when the email was received.
Type: Timestamp
Required: No

 ** SenderHostname **   <a name="sesmailmanager-Type-Row-SenderHostname"></a>
The name of the host from which the email was received.
Type: String
Required: No

 ** SenderIpAddress **   <a name="sesmailmanager-Type-Row-SenderIpAddress"></a>
+ Mail archived with Mail Manager: The IP address of the client that connects to the ingress endpoint.
+ Mail sent through a configuration set with the archiving option enabled: The IP address of the client that makes the SendEmail API call.
Type: String
Required: No

 ** SourceArn **   <a name="sesmailmanager-Type-Row-SourceArn"></a>
Specifies the archived email source, identified by either a Rule Set's ARN with an Archive action, or a Configuration Set's Archive ARN.
Type: String
Required: No

 ** Subject **   <a name="sesmailmanager-Type-Row-Subject"></a>
The subject header value of the email.
Type: String
Required: No

 ** To **   <a name="sesmailmanager-Type-Row-To"></a>
The email addresses in the To header.
Type: String
Required: No

 ** XMailer **   <a name="sesmailmanager-Type-Row-XMailer"></a>
The user agent that sent the email.
Type: String
Required: No

 ** XOriginalMailer **   <a name="sesmailmanager-Type-Row-XOriginalMailer"></a>
The original user agent that sent the email.
Type: String
Required: No

 ** XPriority **   <a name="sesmailmanager-Type-Row-XPriority"></a>
The priority level of the email.
Type: String
Required: No

## See Also
<a name="API_Row_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/Row)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/Row)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/Row)
