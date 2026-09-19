---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/map-application-attributes.html
---

# Map application attributes
<a name="map-application-attributes"></a>

In this step, you map application attributes to the user attribute in IAM Identity Center, using the email address for authentication.

1. From the list of applications, choose the SAML application you created in [Create a SAML 2.0 application](create-saml-app.md).

1. Under **Actions**, choose **Edit attribute mappings**.

1. For the *Subject* **User attribute in the application** row, fill in the two corresponding fields:

<table>
<thead>
  <tr><th>Field</th><th>Value</th></tr>
</thead>
<tbody>
  <tr><td>Maps to this string value or user attribute in IAM Identity Center</td><td>${user:email}</td></tr>
  <tr><td>Format</td><td>emailAddress</td></tr>
</tbody>
</table>

1. Choose **Save Changes**.

**Note**
If you have configured IAM Identity Center to use an external identity provider, you need to ensure that the attribute mappings from external identity provider to IAM Identity Center are configured correctly. For more information refer to [Configuring an external identity provider](configuring-external-idp.md).
