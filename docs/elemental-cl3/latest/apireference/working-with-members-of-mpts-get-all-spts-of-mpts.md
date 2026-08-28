---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/working-with-members-of-mpts-get-all-spts-of-mpts.html
---

# GET List: Get All SPTS of an MPTS
<a name="working-with-members-of-mpts-get-all-spts-of-mpts"></a>

Get a list of all the SPTS programs in the specified MPTS output.

## HTTP Request and Response
<a name="working-with-members-of-mpts-get-all-spts-of-mpts-http-request-response"></a>

### Request URL
<a name="working-with-members-of-mpts-get-all-spts-of-mpts-http-request-response-url"></a>

```
GET http://<Conductor IP address>/mpts/<ID of mpts>/mpts_members
```

### Call Header
<a name="working-with-members-of-mpts-get-all-spts-of-mpts-http-request-response-call-header"></a>
+ Accept: Set to application/xml

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="working-with-members-of-mpts-get-all-spts-of-mpts-http-request-response-response"></a>

The response contains XML content consisting of one `mpts_members` element with the following.
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `mpts_member` elements, one for each mpts member found. Each `mpts_member` element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this MPTS member, assigned by the system when the MPTS member is created (either as part of the creation of an MPTS, or when creating an individual MPTS member). |
| mpts\_id | Integer |  |
| created\_at | String | The time this bulk task was created (the POST Start or Stop was received by the system). <br />Time is in ISO 8601 format, with the timezone designator indicated as an offset from UTC. For example, 2015-08-17T11:59:35-07:00 is the time in the timezone that is 7 hours behind UTC. |
| updated\_at | String | The time the most recent change was made to this task report, in other words, the last time one or more of the count elements was updated.  |
| name | String  | The name (value of the name element) of the channel that is a member of the MPTS. You did not specify this name in the POST MPTS member; instead, the system finds it and includes it in the GET response. |
| Elements created by the POST MPTS Member | See [POST: Create an MPTS](working-with-mpts-create.md). |  |
| input | String  | This is identical to the primary destination that you specified in the profile used to create this channel (which is now an mpts\_member). This primary destination is specified in the profile XML by the following: <br />output\_group/output/udp\_settings/destination/uri <br />output\_group/output/udp\_settings/destination/interface <br />output\_group/output/udp\_settings/destination/username <br />output\_group/output/udp\_settings/destination/password output\_group/output/udp\_settings/destination/certificate file<br />Keep in mind that the *destination *for the profile (channel) becomes *input *for the MPTS.  |
| secondary\_input | String  | This is identical to the secondary destination that you specified in the profile used to create this channel (which is now an mpts\_member). It may be blank. This secondary destination is specified in the profile XML by the following tags: <br />output\_group/output/udp\_settings/secondary\_destination/uri <br />output\_group/output/udp\_settings/secondary\_destination/interface <br />output\_group/output/udp\_settings/secondary\_destination/username <br />output\_group/output/udp\_settings/secondary\_destination/password output\_group/output/udp\_settings/secondary\_destination/certificate file<br />Keep in mind that the *destination *for the profile (channel) becomes *input *for the MPTS.  |
| allocation\_transmit\_destination | String  | This is identical to the following tag that you included in the profile used to create this channel (which is now an mpts\_member):<br />output\_group/output/udp\_settings/allocation\_receipt\_destination <br />Keep in mind that the *receipt *destination for the profile (channel) becomes a *transmit *destination for the MPTS.  |
| complexity\_receipt\_destination | String  | This is identical to the following tag that you included in the profile used to create this channel (which is now an mpts\_member):<br />output\_group/output/udp\_settings/complexity\_transmit\_destination <br />Keep in mind that the *transmit *destination for the profile (channel) becomes a *receipt* destination for the MPTS.  |
| secondary\_allocation\_transmit\_destination | String  | This is identical to the following tag that you included in the profile used to create this channel (which is now an mpts\_member):<br />output\_group/output/udp\_settings/secondary\_allocation\_receipt\_destination<br />Keep in mind that the *receipt *destination for the profile (channel) becomes a *transmit* destination for the MPTS.  |
| secondary\_complexity\_receipt\_destination | String  | This is identical to the following tag that you included in the profile used to create this channel (which is now an mpts\_member):<br />output\_group/output/udp\_settings/secondary\_complexity\_transmit\_destination <br />Keep in mind that the *transmit *destination for the profile (channel) becomes a *receipt* destination for the MPTS.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
