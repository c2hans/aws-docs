---
source_url: https://docs.aws.amazon.com/social-messaging/latest/userguide/receive-message-image.html
---

# Download a media file from WhatsApp to Amazon S3
<a name="receive-message-image"></a>

To retrieve a media file and save it to an Amazon S3 bucket, use the [get-whatsapp-message-media](https://docs.aws.amazon.com/cli/latest/reference/socialmessaging/get-whatsapp-message-media.html) command.

```
aws socialmessaging get-whatsapp-message-media --media-id {{{MEDIA_ID}}} --origination-phone-number-id {{{ORIGINATION_PHONE_NUMBER_ID}}} --destination-s3-file bucketName={{{BUCKET}}},key=inbound_
{
    "mimeType": "image/jpeg",
    "fileSize": 78144
}
```

In the preceding command, do the following:
+ Replace {{{BUCKET}}} with the name of the Amazon S3 bucket.
+ Replace {{{MEDIA\_ID}}} with the value of the `id` field from the received event. For an example incoming media event, see [Example WhatsApp JSON for receiving a media message](managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-media).
+ Replace {{{ORIGINATION\_PHONE\_NUMBER\_ID}}} with your phone number's ID.

To retrieve the media from the Amazon S3 bucket, use the following command:

```
aws s3 cp s3://{{{BUCKET}}}/inbound_{{{MEDIA_ID}}}.jpeg
```

In the preceding command, do the following:
+ Replace {{{BUCKET}}} with the name of the Amazon S3 bucket.
+ Replace {{{MEDIA\_ID}}} with the MEDIA\_ID returned from the previous step.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging Social. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query social-messaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
