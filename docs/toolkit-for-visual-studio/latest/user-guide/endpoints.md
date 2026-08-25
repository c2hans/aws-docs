---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/endpoints.html
---

# Updating firewalls and gateways to allow access
<a name="endpoints"></a>

If you filter access to specific AWS domains or URL endpoints by using a web-content filtering solution, the following endpoints must be allow listed in order to access all of the services and features available through the AWS Toolkit for Visual Studio and Amazon Q. For detailed steps on how to troubleshoot firewall and proxy settings for the AWS Toolkit with Amazon Q, see the [Firewall and proxy settings](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/general-troubleshoot.html#general-troubleshoot-firewall) section in the *Troubleshooting* topic in this User Guide. For detailed information about configuring a corporate proxy for Amazon Q, see the [Configuring a corporate proxy in Amazon Q](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/firewall.html#corp-proxy) topic in the *Amazon Q Developer User Guide*.

## AWS Toolkit for Visual Studio Endpoints
<a name="w2aac13c27b5"></a>

The following are lists of AWS Toolkit for Visual Studio specific endpoints and references that need to be allow listed.

### Endpoints
<a name="w2aac13c27b5b5"></a>

```
https://idetoolkits-hostedfiles.amazonaws.com/*
https://idetoolkits.amazonwebservices.com/*
http://vstoolkit.amazonwebservices.com/*
https://aws-vs-toolkit.s3.amazonaws.com/*
https://raw.githubusercontent.com/aws/aws-toolkit-visual-studio/main/version.json
https://aws-toolkit-language-servers.amazonaws.com/*
```

## Amazon Q plugin endpoints
<a name="w2aac13c27b7"></a>

The following is a list of Amazon Q plugin specific endpoints and references that need to be allow listed.

```
https://idetoolkits-hostedfiles.amazonaws.com/*    (Plugin for configs)
https://idetoolkits.amazonwebservices.com/*   (Plugin for endpoints)
https://aws-toolkit-language-servers.amazonaws.com/*  (Language Server Process)
https://client-telemetry.us-east-1.amazonaws.com/ (Telemetry)
https://cognito-identity.us-east-1.amazonaws.com    (Telemetry)
https://aws-language-servers.us-east-1.amazonaws.com (Language Server Process)
```

## Amazon Q Developer endpoints
<a name="w2aac13c27b9"></a>

The following is a list of Amazon Q Developer specific endpoints and references that need to be allow listed.

```
https://codewhisperer.us-east-1.amazonaws.com (Inline,Chat, QSDA,...)
https://q.us-east-1.amazonaws.com (Inline,Chat, QSDA....)
https://desktop-release.codewhisperer.us-east-1.amazonaws.com/ (Download URL for CLI.)
https://specs.q.us-east-1.amazonaws.com (URL for auto-complete specs used by CLI)
* aws-language-servers.us-east-1.amazonaws.com (Local Workspace context)
```

## Amazon Q Code Transform Endpoints
<a name="w2aac13c27c11"></a>

The following is a list of Amazon Q Code Transform specific endpoints and references that need to be allow listed.

```
https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html
```

## Authentication endpoints
<a name="w2aac13c27c15"></a>

The following is a list of authentication endpoints and references that need to be allow listed.

```
[Directory ID or alias].awsapps.com
* oidc.[Region].amazonaws.com
*.sso.[Region].amazonaws.com
*.sso-portal.[Region].amazonaws.com
*.aws.dev
*.awsstatic.com
*.console.aws.a2z.com
*.sso.amazonaws.com
```

## Identity Endpoints
<a name="w2aac13c27c17"></a>

The following lists contain endpoints that are specific to identity, such as AWS IAM Identity Center and AWS Builder ID.

### AWS IAM Identity Center
<a name="w2aac13c27c17b5"></a>

For details on required endpoints for IAM Identity Center, see the [Enable IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center.html) topic in the *AWS IAM Identity Center* User Guide.

### Enterprise IAM Identity Center
<a name="w2aac13c27c17b7"></a>

```
https://[Center director id].awsapps.com/start (should be permitted to initiate auth)
https://us-east-1.signin.aws (for facilitating authentication, assuming IAM Identity Center is in IAD)
https://oidc.(us-east-1).amazonaws.com
https://log.sso-portal.eu-west-1.amazonaws.com
https://portal.sso.eu-west-1.amazonaws.com
```

### AWS Builder ID
<a name="w2aac13c27c17b9"></a>

```
https://view.awsapps.com/start (must be blocked to disable individual tier)
https://codewhisperer.us-east-1.amazonaws.com and q.us-east-1.amazonaws.com (should be permitted)
```

## Telemetry
<a name="w2aac13c27c19"></a>

The following is a Telemetry specific endpoint that needs to be allow listed.

```
https://telemetry.aws-language-servers.us-east-1.amazonaws.com/
https://client-telemetry.us-east-1.amazonaws.com
```

## References
<a name="w2aac13c27c21"></a>

The following is a list of endpoint references.

```
idetoolkits-hostedfiles.amazonaws.com
cognito-identity.us-east-1.amazonaws.com
amazonwebservices.gallery.vsassets.io
eu-west-1.prod.pr.analytics.console.aws.a2z.com
prod.pa.cdn.uis.awsstatic.com
portal.sso.eu-west-1.amazonaws.com
log.sso-portal.eu-west-1.amazonaws.com
prod.assets.shortbread.aws.dev
prod.tools.shortbread.aws.dev
prod.log.shortbread.aws.dev
a.b.cdn.console.awsstatic.com
assets.sso-portal.eu-west-1.amazonaws.com
oidc.eu-west-1.amazonaws.com
aws-toolkit-language-servers.amazonaws.com
aws-language-servers.us-east-1.amazonaws.com
idetoolkits.amazonwebservices.com
```
