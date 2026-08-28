---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/face-liveness-configure-cutomize-amplify.html
---

# Configuring and Customizing Your Application
<a name="face-liveness-configure-cutomize-amplify"></a>

## Configuring Your Application
<a name="face-liveness-configuring-amplify.title"></a>

Your Face Liveness application can operate on mobile devices or desktop web browsers. You'll want to configure the Face Liveness components to integrate with your chosen solution. You must also ensure your application has permission to use a device's camera. The [ Amplify Liveness guide](https://ui.docs.amplify.aws/react/connected-components/liveness) gives detailed instructions regarding how to:
+  Install and configure AWS Amplify
+  Import and render the FaceLivenessDetector component
+  Listen to callbacks
+  Render Amplify example error messaging

## Customize Your Application
<a name="face-liveness-customize-amplify.title"></a>

You can customize certain components of your liveness application using [AWS Amplify](https://ui.docs.amplify.aws/react/getting-started/introduction).

For information on translation, see the [Amplify Authenticator documentation](https://ui.docs.amplify.aws/react/connected-components/authenticator/customization#internationalization-i18n).

For information on customizing Amplify components and themes, see the Amplify documentation regarding [theming](https://ui.docs.amplify.aws/react/theming).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
