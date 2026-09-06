---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/custom-domains.html
---

# Custom domains
<a name="custom-domains"></a>

When deploying WorkSpaces Applications programmatically, it is possible to create a [custom domain](http://aws.amazon.com/blogs/desktop-and-application-streaming/using-custom-domains-with-amazon-appstream-2-0/) which can provide users with a familiar experience for streaming sessions. In SAML 2.0 IdP deployments of WorkSpaces Applications, it is important to highlight that user access begins at the IdP, not WorkSpaces Applications. Users do not require WorkSpaces Applications URLs, as these are provided by the IdP after authentication. Therefore, custom domain names are not required for SAML 2.0 IdP deployments.
