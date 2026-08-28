---
source_url: https://docs.aws.amazon.com/devicefarm/latest/developerguide/apps.html
---

# Apps in AWS Device Farm
<a name="apps"></a>

The following sections contain information about app behaviors in Device Farm.

**Topics**
+ [Instrumenting apps](#test-runs-instrumenting)
+ [Re-signing apps in runs](#test-runs-app-resigning)
+ [Obfuscated apps in runs](#test-runs-obfuscated-apps)

## Instrumenting apps
<a name="test-runs-instrumenting"></a>

You do not need to instrument your apps or provide Device Farm with the source code for your apps. Android apps can be submitted unmodified. iOS apps must be built with the **iOS Device** target instead of with the simulator.

## Re-signing apps in runs
<a name="test-runs-app-resigning"></a>

For iOS apps, you do not need to add any Device Farm UUIDs to your provisioning profile. Device Farm replaces the embedded provisioning profile with a wildcard profile and then re-signs the app. If you provide auxiliary data, Device Farm adds it to the app's package before Device Farm installs it, so that the auxiliary exists in your app's sandbox. Re-signing the app removes entitlements such as App Group, Associated Domains, Game Center, HealthKit, HomeKit, Wireless Accessory Configuration, In-App Purchase, Inter-App Audio, Apple Pay, Push Notifications, and VPN Configuration & Control.

For Android apps, Device Farm re-signs the app. This might break any functionality that depends on the app's signature, such as the Google Maps Android API, or it might trigger antipiracy or antitamper detection from products such as DexGuard.

## Obfuscated apps in runs
<a name="test-runs-obfuscated-apps"></a>

For Android apps, if the app is obfuscated, you can still test it with Device Farm if you use ProGuard. However, if you use DexGuard with antipiracy measures, Device Farm cannot re-sign and run tests against the app.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
