---
source_url: https://docs.aws.amazon.com/enclaves/latest/user/cmd-nitro-pcr.html
---

# nitro-cli pcr
<a name="cmd-nitro-pcr"></a>

Returns the platform configuration register (PCR) value for a specified input file or PEM certificate. You can use this command to identify the files and signing certificate that were used to sign an enclave by comparing the command output with PCR values in the enclave's build measurements.

## Syntax
<a name="cmd-nitro-pcr-syntax"></a>

```
nitro-cli pcr
    [--input {{path_to_file}}]
    [--signing-certificate {{path_to_certificate}}]
```

## Options
<a name="cmd-nitro-pcr-options"></a>

**`--input`**
The path to the file for which to generate the platform configuration register (PCR) value.
You must specify either `--input` or `--signing-certificate`.
Type: String
Required: Conditional

**`--signing-certificate`**
The path to the PEM certificate for which to generate PCR8. This option is used to specifically request the PCR8 value by performing deserialisation of the certificate and PEM format validation.
You must specify either `--input` or `--signing-certificate`.
Type: String
Required: Conditional

## Output
<a name="cmd-nitro-pcr-output"></a>

**`PCR`**
The platform configuration register (PCR) value for the specified input file or PEM certificate.
Type: String

## Example
<a name="cmd-nitro-pcr-example"></a>

The following example generates the PCR8 value for a PEM certificate named `cert.pem`.

**Command**

```
nitro-cli pcr --signing-certificate {{cert.pem}}
```

**Output**

```
{
    "PCR8": "example39de75e8ed2939e95examplea96f2c79eaf5d5ac3bacf2cb76c75a31f9examplef55b29f0acd256b8example"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query enclaves` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
