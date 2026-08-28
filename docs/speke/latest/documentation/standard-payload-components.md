---
source_url: https://docs.aws.amazon.com/speke/latest/documentation/standard-payload-components.html
---

# SPEKE API v1 - Standard payload components
<a name="standard-payload-components"></a>

In any SPEKE request, the encryptor can request responses for one or more DRM systems. The encryptor specifies the DRM systems in `<cpix:DRMSystemList>` of the request payload. Each system specification includes the key and indicates the type of response to return.

The following example shows a DRM system list with a single DRM system specification:

![RequestIntroSimple](http://docs.aws.amazon.com/speke/latest/documentation/images/RequestIntroSimple.png)

The following table lists the main components of each `<cpix:DRMSystem>`.

| Identifier | Description |
| --- | --- |
|  `systemId` or `schemeId`  | Unique identifier for the DRM system type, as registered with the DASH IF organization. For a list, see [DASH-IF System IDs](https://dashif.org/identifiers/content_protection/). |
|  `kid`  | The key ID. This is not the actual key, but an identifier that points to the key in a hash table. |
|  `<cpix:UriExtXKey>`  | Requests a standard unencrypted key. The key response type must be either this or the `PSSH` response. |
|  `<cpix:PSSH>`  | Requests a Protection System Specific Header (PSSH). This type of header contains a reference to the `kid`, the `systemID`, plus custom data for the DRM vendor, as part of Common Encryption (CENC). The key response type must be either this or the `UriExtXKey` response. |

\_Example Requests for Standard Key and for PSSH \_

The following example shows part of a sample request from the encryptor to the DRM key provider, with the main components highlighted. The first request is for a standard key, while the second request is for a PSSH response:

![RequestIntro1](http://docs.aws.amazon.com/speke/latest/documentation/images/RequestIntro1.png)

\_Example Responses for Standard Key and for PSSH \_

The following example shows the corresponding response from the DRM key provider to the encryptor:

![ResponseIntro1](http://docs.aws.amazon.com/speke/latest/documentation/images/ResponseIntro1.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Packager and Encoder Key Exchange API Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query speke` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
