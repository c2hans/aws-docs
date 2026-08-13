---
source_url: https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.6.20250317.html
---

# Amazon Linux 2023 version 2023.6.20250317 release notes
<a name="relnotes-2023.6.20250317"></a>

These are the release notes for Amazon Linux 2023 (AL2023) version 2023.6.20250317.

**Contents**
+ [Release Summary](#release-summary-2023.6.20250317)
+ [Repository](#amis-2023.6.20250317.repository)
  + [New packages in AL2023.6.20250317 since AL2023.6.20250303](#new-AL2023.6.20250303-AL2023.6.20250317)
  + [AL2023.6.20250317 upgrades from AL2023.6.20250303](#vercmp-AL2023.6.20250303-AL2023.6.20250317)
+ [Image Updates](#ami-updates-2023.6.20250317)
  + [Default AMI](#amis-2023.6.20250317.default-ami)
  + [Default Container](#amis-2023.6.20250317.default-container)
  + [Minimal AMI](#amis-2023.6.20250317.minimal-ami)
  + [Minimal Container](#amis-2023.6.20250317.minimal-container)
+ [Contact us](#amis-2023.6.20250317.contact-us)

## Release Summary
<a name="release-summary-2023.6.20250317"></a>

This release represents an update to the 6th quarterly release of AL2023. AL2023 is the next generation of Amazon Linux. It comes with five years of support and brings features such as deterministic updates and better optimizations for Graviton processors into Amazon Linux. AL2023 is ready for production workloads, and you can start migrating from previous versions of Amazon Linux today.

**Known issues**
+  AL2023 is not yet FIPS certified. AL2023 is in the process of being certified for FIPS 140-3.

**Security updates**
+ For information on the CVEs addressed in this release, see the [ Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html).
+ For visibility into the status of CVEs that haven't been addressed yet, see the [ Amazon Linux Security Center](https://explore.alas.aws.amazon.com/).

## Repository
<a name="amis-2023.6.20250317.repository"></a>

### New packages in AL2023.6.20250317 since AL2023.6.20250303
<a name="new-AL2023.6.20250303-AL2023.6.20250317"></a>

 Comparing AL2023.6.20250303 version 2023.6.20250303 to AL2023.6.20250317 version [2023.6.20250317](#relnotes-2023.6.20250317).

| Package Type | Number of new packages in AL2023.6.20250317 compared to AL2023.6.20250303 |
| --- | --- |
| Source RPMs | 53 |
| Total Binary RPMs | 287 |
|  noarch binary RPMs | 40 |
|  x86\_64 binary RPMs | 124 |
|  aarch64 binary RPMs | 123 |

New packages in AL2023.6.20250317:

- ** `accountsservice` **
  - **RPM:**  accountsservice  / **Architectures:** aarch64, x86\_64
  - **RPM:**  accountsservice-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  accountsservice-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 23.13.9-5.amzn2023

- ** `adwaita-icon-theme-legacy` **
  - **RPM:**  adwaita-icon-theme-legacy  / **Architectures:** noarch
  - **RPM:**  adwaita-icon-theme-legacy-devel  / **Architectures:** noarch
  - **Version:** 46.2-2.amzn2023

- ** `amazon-linux-logos` **
  - **RPM:**  amazon-linux-logos
  - **Architectures:** noarch
  - **Version:** 0.3-1.amzn2023

- ** `colord-gtk` **
  - **RPM:**  colord-gtk  / **Architectures:** aarch64, x86\_64
  - **RPM:**  colord-gtk4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  colord-gtk4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  colord-gtk-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.3.1-2.amzn2023

- ** `dconf-editor` **
  - **RPM:**  dconf-editor
  - **Architectures:** aarch64, x86\_64
  - **Version:** 45.0.1-5.amzn2023.0.1

- ** `evolution-data-server` **
  - **RPM:**  evolution-data-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  evolution-data-server-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  evolution-data-server-doc  / **Architectures:** noarch
  - **RPM:**  evolution-data-server-langpacks  / **Architectures:** noarch
  - **RPM:**  evolution-data-server-perl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  evolution-data-server-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.54.3-1.amzn2023.0.1

- ** `fdk-aac-free` **
  - **RPM:**  fdk-aac-free  / **Architectures:** aarch64, x86\_64
  - **RPM:**  fdk-aac-free-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 2.0.0-14.amzn2023.0.1

- ** `firefox` **
  - **RPM:**  firefox
  - **Architectures:** aarch64, x86\_64
  - **Version:** 128.7.0-1.amzn2023.0.2

- ** [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  gcc-plugin-annobin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcc1  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nvptx-common  / **Architectures:** x86\_64
  - **Version:** 11.5.0-5.amzn2023.0.1

- ** `gcr` **
  - **RPM:**  gcr-libs
  - **Architectures:** aarch64, x86\_64
  - **Version:** 4.3.0-3.amzn2023.0.1

- ** `gdm` **
  - **RPM:**  gdm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gdm-pam-extensions-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 47.0-970.amzn2023

- ** `gjs` **
  - **RPM:**  gjs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gjs-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gjs-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.80.2-11.amzn2023.0.1

- ** `glycin` **
  - **RPM:**  glycin-loaders
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-6.amzn2023

- ** `gnome-autoar` **
  - **RPM:**  gnome-autoar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-autoar-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.4.5-1.amzn2023.0.1

- ** `gnome-backgrounds` **
  - **RPM:**  gnome-backgrounds  / **Architectures:** noarch
  - **RPM:**  gnome-backgrounds-extras  / **Architectures:** noarch
  - **Version:** 47.0-1.amzn2023

- ** `gnome-control-center` **
  - **RPM:**  gnome-control-center  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-control-center-filesystem  / **Architectures:** noarch
  - **Version:** 47.3-194.amzn2023

- ** `gnome-desktop3` **
  - **RPM:**  gnome-desktop3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-desktop3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-desktop3-tests  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-desktop4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-desktop4-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 44.1-332.amzn2023

- ** `gnome-extensions-app` **
  - **RPM:**  gnome-extensions-app
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.2-52.amzn2023

- ** `gnome-keyring` **
  - **RPM:**  gnome-keyring  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-keyring-pam  / **Architectures:** aarch64, x86\_64
  - **Version:** 46.2-341.amzn2023

- ** `gnome-menus` **
  - **RPM:**  gnome-menus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-menus-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.36.0-12.amzn2023.0.1

- ** `gnome-online-accounts` **
  - **RPM:**  gnome-online-accounts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-online-accounts-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 3.53.0-253.amzn2023.0.1

- ** `gnome-remote-desktop` **
  - **RPM:**  gnome-remote-desktop
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.3-1.amzn2023

- ** `gnome-session` **
  - **RPM:**  gnome-session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-session-wayland-session  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-session-xsession  / **Architectures:** aarch64, x86\_64
  - **Version:** 47.0.1-575.amzn2023

- ** `gnome-settings-daemon` **
  - **RPM:**  gnome-settings-daemon  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gnome-settings-daemon-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 47.2-608.amzn2023

- ** `gnome-shell` **
  - **RPM:**  gnome-shell
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.3-705.amzn2023

- ** `gnome-shell-extension-dash-to-dock` **
  - **RPM:**  gnome-shell-extension-dash-to-dock
  - **Architectures:** noarch
  - **Version:** 99-77.amzn2023

- ** `gnome-shell-extensions` **
  - **RPM:**  gnome-classic-session  / **Architectures:** noarch
  - **RPM:**  gnome-classic-session-xsession  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-apps-menu  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-auto-move-windows  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-common  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-drive-menu  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-launch-new-instance  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-light-style  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-native-window-placement  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-places-menu  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-screenshot-window-sizer  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-status-icons  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-system-monitor  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-user-theme  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-window-list  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-windowsNavigator  / **Architectures:** noarch
  - **RPM:**  gnome-shell-extension-workspace-indicator  / **Architectures:** noarch
  - **Version:** 47.1-275.amzn2023

- ** `gnome-system-monitor` **
  - **RPM:**  gnome-system-monitor
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.0-1.amzn2023

- ** `gnome-tweaks` **
  - **RPM:**  gnome-tweaks
  - **Architectures:** noarch
  - **Version:** 46.1-3.amzn2023

- ** `gsound` **
  - **RPM:**  gsound  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gsound-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.0.3-9.amzn2023.0.1

- ** `gstreamer1-plugins-bad-free` **
  - **RPM:**  gstreamer1-plugins-bad-free  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-bad-free-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gstreamer1-plugins-bad-free-libs  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.24.10-1.amzn2023.0.3

- ** `gtk4` **
  - **RPM:**  gtk4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtk4-devel-docs  / **Architectures:** noarch
  - **RPM:**  gtk4-devel-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 4.16.5-173.amzn2023

- ** `gtkmm4.0` **
  - **RPM:**  gtkmm4.0  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtkmm4.0-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gtkmm4.0-doc  / **Architectures:** noarch
  - **Version:** 4.16.0-30.amzn2023

- ** `gvfs` **
  - **RPM:**  gvfs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-archive  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-fuse  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-goa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-nfs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gvfs-smb  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.56.1-1.amzn2023.0.1

- ** `libadwaita` **
  - **RPM:**  libadwaita  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libadwaita-demo  / **Architectures:** noarch
  - **RPM:**  libadwaita-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libadwaita-doc  / **Architectures:** noarch
  - **Version:** 1.6.2-1.amzn2023

- ** `libdisplay-info` **
  - **RPM:**  libdisplay-info  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdisplay-info-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libdisplay-info-tools  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.2.0-2.amzn2023.0.1

- ** `libportal` **
  - **RPM:**  libportal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libportal-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libportal-devel-doc  / **Architectures:** noarch
  - **RPM:**  libportal-gtk3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libportal-gtk3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libportal-gtk4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libportal-gtk4-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.9.0-1.amzn2023.0.1

- ** `libxslt` **
  - **RPM:**  python3-libxslt
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.42-3.amzn2023

- ** `mariadb-connector-c` **
  - **RPM:**  mariadb-connector-c-doc
  - **Architectures:** noarch
  - **Version:** 3.3.10-1.amzn2023.0.1

- ** `mutter` **
  - **RPM:**  mutter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mutter-common  / **Architectures:** noarch
  - **RPM:**  mutter-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mutter-tests  / **Architectures:** aarch64, x86\_64
  - **Version:** 47.4-586.amzn2023

- ** `nautilus` **
  - **RPM:**  nautilus  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nautilus-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nautilus-extensions  / **Architectures:** aarch64, x86\_64
  - **Version:** 47.1-718.amzn2023

- ** `nv-codec-headers` **
  - **RPM:**  nv-codec-headers
  - **Architectures:** noarch
  - **Version:** 12.2.72.0-1.amzn2023

- ** `pinentry` **
  - **RPM:**  pinentry-gnome3
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.3.1-2.amzn2023.0.1

- ** `plymouth` **
  - **RPM:**  plymouth  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-core-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-graphics-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-fade-throbber  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-label  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-script  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-space-flares  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-plugin-two-step  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-scripts  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-system-theme  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-fade-in  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-script  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-solar  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-spinfinity  / **Architectures:** aarch64, x86\_64
  - **RPM:**  plymouth-theme-spinner  / **Architectures:** aarch64, x86\_64
  - **Version:** 24.004.60-330.amzn2023

- ** `ptyxis` **
  - **RPM:**  ptyxis
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.6-18.amzn2023

- ** `rest0.7` **
  - **RPM:**  rest0.7  / **Architectures:** aarch64, x86\_64
  - **RPM:**  rest0.7-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.8.1-6.amzn2023.0.1

- ** `seahorse` **
  - **RPM:**  seahorse
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.0.1-1.amzn2023

- ** `spice-protocol` **
  - **RPM:**  spice-protocol
  - **Architectures:** noarch
  - **Version:** 0.14.4-6.amzn2023

- ** `spice-vdagent` **
  - **RPM:**  spice-vdagent
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.22.1-7.amzn2023

- ** `switcheroo-control` **
  - **RPM:**  switcheroo-control  / **Architectures:** aarch64, x86\_64
  - **RPM:**  switcheroo-control-docs  / **Architectures:** noarch
  - **Version:** 2.6-7.amzn2023

- ** `tecla` **
  - **RPM:**  tecla  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tecla-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 45.0-9.amzn2023

- ** `tigervnc` **
  - **RPM:**  tigervnc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tigervnc-icons  / **Architectures:** noarch
  - **RPM:**  tigervnc-license  / **Architectures:** noarch
  - **RPM:**  tigervnc-selinux  / **Architectures:** noarch
  - **RPM:**  tigervnc-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tigervnc-server-minimal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  tigervnc-server-module  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.14.1-3.amzn2023.0.1

- ** `vte291` **
  - **RPM:**  vte291  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vte291-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vte291-gtk4  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vte291-gtk4-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  vte-profile  / **Architectures:** aarch64, x86\_64
  - **Version:** 0.78.2-1.amzn2023.0.1

- ** `xcalc` **
  - **RPM:**  xcalc
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.1.2-42.amzn2023

- ** `xdg-desktop-portal` **
  - **RPM:**  xdg-desktop-portal  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xdg-desktop-portal-devel  / **Architectures:** aarch64, x86\_64
  - **Version:** 1.18.4-105.amzn2023

- ** `xdg-desktop-portal-gnome` **
  - **RPM:**  xdg-desktop-portal-gnome
  - **Architectures:** aarch64, x86\_64
  - **Version:** 47.1-48.amzn2023

- ** `xdg-desktop-portal-gtk` **
  - **RPM:**  xdg-desktop-portal-gtk
  - **Architectures:** aarch64, x86\_64
  - **Version:** 1.15.1-61.amzn2023

- ** `xdg-user-dirs-gtk` **
  - **RPM:**  xdg-user-dirs-gtk
  - **Architectures:** aarch64, x86\_64
  - **Version:** 0.11-5.amzn2023.0.1

### AL2023.6.20250317 upgrades from AL2023.6.20250303
<a name="vercmp-AL2023.6.20250303-AL2023.6.20250317"></a>

 Comparing [2023.6.20250303](relnotes-2023.6.20250303.md) to [2023.6.20250317](#relnotes-2023.6.20250317).

| Package Type | Count |
| --- | --- |
| Source | 30 |
| Total Binary | 337 |
|  noarch binary RPMs | 80 |
|  x86\_64 binary RPMs | 131 |
|  aarch64 binary RPMs | 126 |

The full comparison of RPM package versions is below.

- ** `adwaita-icon-theme` **
  - **RPM:**  adwaita-cursor-theme  / **Architectures:** noarch
  - **RPM:**  adwaita-icon-theme  / **Architectures:** noarch
  - **RPM:**  adwaita-icon-theme-devel  / **Architectures:** noarch
  - **AL2023.6.20250303 version:** 40.1.1-1.amzn2023.0.2
  - **AL2023.6.20250317 version:** 47.0-1.amzn2023.0.1

- ** `amazon-rpm-config` **
  - **RPM:**  amazon-rpm-config
  - **Architectures:** noarch
  - **AL2023.6.20250303 version:** 228-4.amzn2023.0.1
  - **AL2023.6.20250317 version:** 228-7.amzn2023.0.1

- ** `ansible-core` **
  - **RPM:**  ansible-core  / **Architectures:** aarch64, x86\_64
  - **RPM:**  ansible-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 2.15.3-1.amzn2023.0.8
  - **AL2023.6.20250317 version:** 2.15.3-1.amzn2023.0.10

- ** `aws-cfn-bootstrap` **
  - **RPM:**  aws-cfn-bootstrap
  - **Architectures:** noarch
  - **AL2023.6.20250303 version:** 2.0-32.amzn2023
  - **AL2023.6.20250317 version:** 2.0-33.amzn2023

- ** `awscli-2` **
  - **RPM:**  awscli-2
  - **Architectures:** noarch
  - **AL2023.6.20250303 version:** 2.17.18-1.amzn2023.0.1
  - **AL2023.6.20250317 version:** 2.23.11-1.amzn2023.0.1

- ** `credentials-fetcher` **
  - **RPM:**  credentials-fetcher
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.3.7-0.amzn2023
  - **AL2023.6.20250317 version:** 1.3.8-0.amzn2023

- ** `dnf-plugin-support-info` **
  - **RPM:**  dnf-plugin-support-info
  - **Architectures:** noarch
  - **AL2023.6.20250303 version:** 1.3-1.amzn2023
  - **AL2023.6.20250317 version:** 1.4-1.amzn2023

- ** [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html) **
  - **RPM:**  [`ecs-init`](https://docs.aws.amazon.com/linux/al2023/ug/ecs.html)
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.90.0-1.amzn2023
  - **AL2023.6.20250317 version:** 1.91.0-1.amzn2023

- ** [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html) **
  - **RPM:**  cpp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  [`gcc`](https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-c\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gdb-plugin  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-gfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcc-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  gcc-plugin-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libasan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libatomic-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgcc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgccjit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgfortran-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libgomp-offload-nvptx  / **Architectures:** x86\_64
  - **RPM:**  libitm  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libitm-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  liblsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libquadmath  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-devel  / **Architectures:** x86\_64
  - **RPM:**  libquadmath-static  / **Architectures:** x86\_64
  - **RPM:**  libstdc\+\+  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-docs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libstdc\+\+-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libtsan-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libubsan-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 11.4.1-2.amzn2023.0.2
  - **AL2023.6.20250317 version:** 11.5.0-5.amzn2023.0.1

- ** `gcr` **
  - **RPM:**  gcr  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gcr-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 3.40.0-1.amzn2023.0.3
  - **AL2023.6.20250317 version:** 4.3.0-3.amzn2023.0.1

- ** `glib2` **
  - **RPM:**  glib2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  glib2-tests  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 2.82.2-764.amzn2023
  - **AL2023.6.20250317 version:** 2.82.2-765.amzn2023

- ** `gssdp` **
  - **RPM:**  gssdp  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gssdp-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  gssdp-docs  / **Architectures:** noarch
  - **RPM:**  gssdp-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.2.3-3.amzn2023.0.3
  - **AL2023.6.20250317 version:** 1.6.3-3.amzn2023.0.1

- ** `kernel` **
  - **RPM:**  bpftool  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-headers  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-libbpf-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-modules-extra-common  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools  / **Architectures:** aarch64, x86\_64
  - **RPM:**  kernel-tools-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  perf  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-perf  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 6.1.129-138.220.amzn2023
  - **AL2023.6.20250317 version:** 6.1.130-139.222.amzn2023

- ** `libcap` **
  - **RPM:**  libcap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libcap-static  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 2.48-2.amzn2023.0.3
  - **AL2023.6.20250317 version:** 2.48-2.amzn2023.0.4

- ** `libpsl` **
  - **RPM:**  libpsl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libpsl-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  psl  / **Architectures:** aarch64, x86\_64
  - **RPM:**  psl-make-dafsa  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 0.21.1-3.amzn2023.0.2
  - **AL2023.6.20250317 version:** 0.21.5-1.amzn2023.0.1

- ** `libsndfile` **
  - **RPM:**  libsndfile  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libsndfile-utils  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.2.2-3.amzn2023.0.2
  - **AL2023.6.20250317 version:** 1.2.2-3.amzn2023.0.3

- ** `libxml2` **
  - **RPM:**  libxml2  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxml2-static  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libxml2  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 2.10.4-1.amzn2023.0.8
  - **AL2023.6.20250317 version:** 2.10.4-1.amzn2023.0.9

- ** `libxslt` **
  - **RPM:**  libxslt  / **Architectures:** aarch64, x86\_64
  - **RPM:**  libxslt-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.1.34-5.amzn2023.0.2
  - **AL2023.6.20250317 version:** 1.1.42-3.amzn2023

- ** `mariadb-connector-c` **
  - **RPM:**  mariadb-connector-c  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb-connector-c-config  / **Architectures:** noarch
  - **RPM:**  mariadb-connector-c-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  mariadb-connector-c-test  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 3.1.13-1.amzn2023.0.3
  - **AL2023.6.20250317 version:** 3.3.10-1.amzn2023.0.1

- ** `nano` **
  - **RPM:**  default-editor  / **Architectures:** noarch
  - **RPM:**  nano  / **Architectures:** aarch64, x86\_64
  - **RPM:**  nano-default-editor  / **Architectures:** noarch
  - **AL2023.6.20250303 version:** 5.8-3.amzn2023.0.4
  - **AL2023.6.20250317 version:** 8.3-1.amzn2023

- ** `pinentry` **
  - **RPM:**  pinentry  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pinentry-emacs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pinentry-tty  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.2.0-1.amzn2023.0.5
  - **AL2023.6.20250317 version:** 1.3.1-2.amzn2023.0.1

- ** `pipewire` **
  - **RPM:**  pipewire  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-alsa  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-config-rates  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-config-upmix  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-doc  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-gstreamer  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-jack-audio-connection-kit  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-jack-audio-connection-kit-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-jack-audio-connection-kit-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-module-x11  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-plugin-vulkan  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-pulseaudio  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-utils  / **Architectures:** aarch64, x86\_64
  - **RPM:**  pipewire-v4l2  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 1.2.7-1.amzn2023.0.1
  - **AL2023.6.20250317 version:** 1.2.7-4.amzn2023.0.3

- ** [`python3.12`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  [`python3.12`](https://docs.aws.amazon.com/linux/al2023/ug/python.html)  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3.12-tkinter  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 3.12.8-1.amzn2023.0.1
  - **AL2023.6.20250317 version:** 3.12.9-1.amzn2023.0.1

- ** [`python3.9`](https://docs.aws.amazon.com/linux/al2023/ug/python.html) **
  - **RPM:**  python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-debug  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-idle  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-libs  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-test  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python3-tkinter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  python-unversioned-command  / **Architectures:** noarch
  - **AL2023.6.20250303 version:** 3.9.20-1.amzn2023.0.3
  - **AL2023.6.20250317 version:** 3.9.21-1.amzn2023.0.2

- ** `python-awscrt` **
  - **RPM:**  python3-awscrt
  - **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 0.19.19-1.amzn2023.0.1
  - **AL2023.6.20250317 version:** 0.23.8-1.amzn2023.0.1

- ** `python-jinja2` **
  - **RPM:**  python3-jinja2
  - **Architectures:** noarch
  - **AL2023.6.20250303 version:** 2.11.3-1.amzn2023.0.5
  - **AL2023.6.20250317 version:** 2.11.3-1.amzn2023.0.6

- ** `python-twisted` **
  - **RPM:**  python3-twisted  / **Architectures:** noarch
  - **RPM:**  python3-twisted\+tls  / **Architectures:** noarch
  - **AL2023.6.20250303 version:** 22.4.0-127.amzn2023.0.4
  - **AL2023.6.20250317 version:** 22.4.0-128.amzn2023.0.5

- ** `system-release` **
  - **RPM:**  amazon-linux-repo-cdn  / **Architectures:** noarch
  - **RPM:**  amazon-linux-repo-s3  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-cdn  / **Architectures:** noarch
  - **RPM:**  kernel-livepatch-repo-s3  / **Architectures:** noarch
  - **RPM:**  system-release  / **Architectures:** noarch
  - **AL2023.6.20250303 version:** 2023.6.20250303-0.amzn2023
  - **AL2023.6.20250317 version:** 2023.6.20250317-0.amzn2023

- ** `systemtap` **
  - **RPM:**  systemtap  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-client  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-exporter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-initscript  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-jupyter  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-java  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-python3  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-runtime-virtguest  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-devel  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-sdt-dtrace  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-server  / **Architectures:** aarch64, x86\_64
  - **RPM:**  systemtap-testsuite  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 5.2-1.amzn2023.0.3
  - **AL2023.6.20250317 version:** 5.2-1.amzn2023.0.4

- ** `xorg-x11-server-Xwayland` **
  - **RPM:**  xorg-x11-server-Xwayland  / **Architectures:** aarch64, x86\_64
  - **RPM:**  xorg-x11-server-Xwayland-devel  / **Architectures:** aarch64, x86\_64
  - **AL2023.6.20250303 version:** 24.1.3-1.amzn2023
  - **AL2023.6.20250317 version:** 24.1.3-1.amzn2023.0.1

## Image Updates
<a name="ami-updates-2023.6.20250317"></a>

### Default AMI
<a name="amis-2023.6.20250317.default-ami"></a>

This section provides details about default ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.6.20250317-0.amzn2023  |
|  amazon-rpm-config-228-7.amzn2023.0.1  |
|  aws-cfn-bootstrap-2.0-33.amzn2023  |
|  awscli-2-2.23.11-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.4-1.amzn2023  |
|  glib2-2.82.2-765.amzn2023  |
|  kernel-libbpf-6.1.130-139.222.amzn2023  |
|  kernel-livepatch-repo-s3-2023.6.20250317-0.amzn2023  |
|  kernel-tools-6.1.130-139.222.amzn2023  |
|  kernel-6.1.130-139.222.amzn2023  |
|  libcap-2.48-2.amzn2023.0.4  |
|  libgcc-11.5.0-5.amzn2023.0.1  |
|  libgomp-11.5.0-5.amzn2023.0.1  |
|  libpsl-0.21.5-1.amzn2023.0.1  |
|  libstdc\+\+-11.5.0-5.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.9  |
|  nano-8.3-1.amzn2023  |
|  python3-awscrt-0.23.8-1.amzn2023.0.1  |
|  python3-jinja2-2.11.3-1.amzn2023.0.6  |
|  python3-libs-3.9.21-1.amzn2023.0.2  |
|  python3-3.9.21-1.amzn2023.0.2  |
|  system-release-2023.6.20250317-0.amzn2023  |
|  systemtap-runtime-5.2-1.amzn2023.0.4  |

### Default Container
<a name="amis-2023.6.20250317.default-container"></a>

This section provides details about default container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.6.20250317-0.amzn2023  |
|  glib2-2.82.2-765.amzn2023  |
|  libcap-2.48-2.amzn2023.0.4  |
|  libgcc-11.5.0-5.amzn2023.0.1  |
|  libgomp-11.5.0-5.amzn2023.0.1  |
|  libpsl-0.21.5-1.amzn2023.0.1  |
|  libstdc\+\+-11.5.0-5.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.9  |
|  python3-libs-3.9.21-1.amzn2023.0.2  |
|  python3-3.9.21-1.amzn2023.0.2  |
|  system-release-2023.6.20250317-0.amzn2023  |

### Minimal AMI
<a name="amis-2023.6.20250317.minimal-ami"></a>

This section provides details about minimal ami.

|  |
| --- |
|  amazon-linux-repo-s3-2023.6.20250317-0.amzn2023  |
|  awscli-2-2.23.11-1.amzn2023.0.1  |
|  dnf-plugin-support-info-1.4-1.amzn2023  |
|  glib2-2.82.2-765.amzn2023  |
|  kernel-libbpf-6.1.130-139.222.amzn2023  |
|  kernel-livepatch-repo-s3-2023.6.20250317-0.amzn2023  |
|  kernel-6.1.130-139.222.amzn2023  |
|  libcap-2.48-2.amzn2023.0.4  |
|  libgcc-11.5.0-5.amzn2023.0.1  |
|  libgomp-11.5.0-5.amzn2023.0.1  |
|  libpsl-0.21.5-1.amzn2023.0.1  |
|  libstdc\+\+-11.5.0-5.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.9  |
|  python3-awscrt-0.23.8-1.amzn2023.0.1  |
|  python3-jinja2-2.11.3-1.amzn2023.0.6  |
|  python3-libs-3.9.21-1.amzn2023.0.2  |
|  python3-3.9.21-1.amzn2023.0.2  |
|  system-release-2023.6.20250317-0.amzn2023  |

### Minimal Container
<a name="amis-2023.6.20250317.minimal-container"></a>

This section provides details about minimal container.

|  |
| --- |
|  amazon-linux-repo-cdn-2023.6.20250317-0.amzn2023  |
|  glib2-2.82.2-765.amzn2023  |
|  libcap-2.48-2.amzn2023.0.4  |
|  libgcc-11.5.0-5.amzn2023.0.1  |
|  libpsl-0.21.5-1.amzn2023.0.1  |
|  libstdc\+\+-11.5.0-5.amzn2023.0.1  |
|  libxml2-2.10.4-1.amzn2023.0.9  |
|  system-release-2023.6.20250317-0.amzn2023  |

## Contact us
<a name="amis-2023.6.20250317.contact-us"></a>

If you find a security issue, contact [our security team](https://github.com/amazonlinux/amazon-linux-2023/security/policy) instead of opening a GitHub issue.

We use GitHub issues to gather feedback about AL2023 and to track bug reports and feature requests. You can look at [existing issues](https://github.com/amazonlinux/amazon-linux-2023/issues) to see whether your concern is already known. If it is not, open a [new issue](https://github.com/amazonlinux/amazon-linux-2023/issues/new/choose).

If you only have questions about AL2023, feel free to start or join a [discussion](https://github.com/amazonlinux/amazon-linux-2023/discussions). Feedback on AL2023 can also be provided through your designated AWS representative.
