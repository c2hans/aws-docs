---
source_url: https://docs.aws.amazon.com/ses/latest/dg/header-fields.html
---

# Amazon SES header fields
<a name="header-fields"></a>

Amazon SES can accept all email headers that follow the format described in [RFC 822](https://www.rfc-editor.org/rfc/rfc822.html).

The following fields can't appear more than once in the header section of a message:
+ `Accept-Language`
+ `acceptLanguage`
+ `Archived-At`
+ `Auto-Submitted`
+ `Bounces-to`
+ `Comments`
+ `Content-Alternative`
+ `Content-Base`
+ `Content-Class`
+ `Content-Description`
+ `Content-Disposition`
+ `Content-Duration`
+ `Content-ID`
+ `Content-Language`
+ `Content-Length`
+ `Content-Location`
+ `Content-MD5`
+ `Content-Transfer-Encoding`
+ `Content-Type`
+ `Date`
+ `Delivered-To `
+ `Disposition-Notification-Options`
+ `Disposition-Notification-To`
+ `DKIM-Signature`
+ `DomainKey-Signature`
+ `Errors-To`
+ `From`
+ `Importance`
+ `In-Reply-To`
+ `Keywords`
+ `List-Archive`
+ `List-Help`
+ `List-Id`
+ `List-Owner`
+ `List-Post`
+ `List-Subscribe`
+ `List-Unsubscribe`
+ `List-Unsubscribe-Post`
+ `Message-Context`
+ `Message-ID`
+ `MIME-Version`
+ `Organization`
+ `Original-From`
+ `Original-Message-ID`
+ `Original-Recipient`
+ `Original-Subject`
+ `Precedence`
+ `Priority`
+ `References`
+ `Reply-To`
+ `Return-Path`
+ `Return-Receipt-To`
+ `Sender`
+ `Solicitation`
+ `Sensitivity`
+ `Subject`
+ `Thread-Index`
+ `Thread-Topic`
+ `User-Agent`
+ `VBR-Info`

**Considerations**
+ The `acceptLanguage` field is non-standard. If possible, you should use the `Accept-Language` header instead.
+ If you specify a `Date` header, Amazon SES overrides it with a timestamp that corresponds to the date and time in the UTC time zone when Amazon SES accepted the message.
+ If you provide a `Message-ID` header, Amazon SES overrides the header with its own value.
+ If you specify a `Return-Path` header, Amazon SES sends bounce and complaint notifications to the address that you specified. However, the message that your recipients receive contains a different value for the `Return-Path` header.
+ If you use the Amazon SES API v2 `SendEmail` operation with either *Simple* or *Templated* content, or use the `SendBulkEmail` operation, you cannot set custom header content for headers that are set by SES; therefore, the following headers are disallowed as custom headers:
  + `BCC`, `CC`, `Content-Disposition`, `Content-Type`, `Date`, `From`, `Message-ID`, `MIME-Version`, `Reply-To`, `Return-Path`, `Subject`, `To`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
