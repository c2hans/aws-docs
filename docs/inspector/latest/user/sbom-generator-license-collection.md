---
source_url: https://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html
---

# Amazon Inspector SBOM Generator license collection
<a name="sbom-generator-license-collection"></a>

 The Amazon Inspector SBOM Generator helps track license information in a software bill of materials (SBOM). It collects license information from supported packages across operating systems and programming languages. With standardized license expressions in your generated SBOM, you can understand your licensing obligations.

## Collect license information
<a name="w2aac39c31b5"></a>

**Example command**
 The following example shows how to collect license information from a directory.

```
./inspector-sbomgen directory --path /path/to/your/directory/ --collect-licenses
```

**SBOM component example**
 The following example shows a component entry in the generated SBOM.

```
"components": [
    {
      "bom-ref": "comp-2",
      "type": "application",
      "name": "sample-js-pkg",
      "version": "1.2.3",
      "licenses": [
        {
          "expression": "Apache-2.0 AND (MIT OR GPL-2.0-only)"
        }
      ],
      "purl": "pkg:npm/sample-js-pkg@1.2.3",
    }
  ]
```

## Supported packages
<a name="w2aac39c31b7"></a>

 The following programming languages and operating system packages are supported for license collection.

| Target | Package manager | License information source | Type |
| --- | --- | --- | --- |
| Alma Linux | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| Amazon Linux | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| CentOS | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| Fedora | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| OpenSUSE | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| Oracle Linux | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| Photon OS | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| RHEL | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| Rocky Linux | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| SLES | RPM |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | OS |
| Alpine Linux | APK | /lib/apk/db/installed | OS |
| Chainguard | APK | /lib/apk/db/installed | OS |
| Debian | DPKG | /usr/share/doc/\*/copyright | OS |
| Ubuntu | DPKG | /usr/share/doc/\*/copyright | OS |
| Node.js | Javascript | node\_modules/\*/package.json | Programing language |
| PHP | Composer package |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | Programing language |
| Go | Go | LICENSE | Programing language |
| Python | Python/Egg/Wheel |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/inspector/latest/user/sbom-generator-license-collection.html)  | Programing language |
| Ruby | RubyGem | \*.gemspec | Programing language |
| Rust | crate | Cargo.toml | Programming language |

### License expression standardization
<a name="w2aac39c31b7b7"></a>

 The SPDX license expressions format provides accurate representation of licensing terms found in open source software. The Amazon Inspector SBOM Generator standardizes all license information into SPDX license expressions through rules described in this section. The rules provide consistency and compatibility across licensing information.

**SPDX short form identifier mapping**
 All license names are mapped to SPDX short form identifiers. For example, `MIT License` is shortened to `MIT`.

**Multiple license combination**
 You can combine more than one license with the `AND` operator. The following is an example command showing how to format your command.

```
MIT AND Apache-2.0
```

**Custom license prefix**
 Custom licenses are prefixed with `LicenseRef`, such as `LicenseRef-CompanyPrivate`.

**Custom exception prefix**
 Custom exceptions are prefixed with `AdditionRef-`, such as `AdditionRef-CustomException`.
