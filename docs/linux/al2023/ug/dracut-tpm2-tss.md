---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/dracut-tpm2-tss.html
---

# Resolving a dracut error about the `systemd-pcrphase` module and `tpm2-tss`
<a name="dracut-tpm2-tss"></a>

When you rebuild the initramfs on AL2023 (for example, by running `sudo dracut --force` or as part of a kernel package installation), **dracut** might fail with the following error:

```
$ sudo dracut --force
dracut[E]: Module 'systemd-pcrphase' depends on 'tpm2-tss', which can't be installed
```

This error can occur even when the `tpm2-tss` package is already installed on your instance.

## Cause
<a name="dracut-tpm2-tss-cause"></a>

The `systemd-pcrphase` dracut module measures boot phases into a Trusted Platform Module (TPM). In addition to `tpm2-tss`, the module also requires the `tpm2-tools` and `tpm2-tss-fapi` packages to be present before it can be included in the initramfs. These packages are not installed by default on AL2023, so installing `tpm2-tss` on its own does not resolve the error.

## Resolution
<a name="dracut-tpm2-tss-resolution"></a>

Install the missing tpm2 packages, and then rebuild the initramfs.

1. Install the `tpm2-tss-fapi` and `tpm2-tools` packages:

   ```
   $ sudo dnf install tpm2-tss-fapi tpm2-tools
   ```

1. Rebuild the initramfs. The command now completes without the `systemd-pcrphase` error:

   ```
   $ sudo dracut --force
   ```

**Note**
AL2023 does not install the `tpm2-tools` and `tpm2-tss-fapi` packages by default, and there are no plans to include them in the default AL2023 AMIs. If you need the `systemd-pcrphase` dracut module, install these packages manually as shown above.
