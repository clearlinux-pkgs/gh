#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gh
Version  : 2.22.0
Release  : 46
URL      : https://github.com/cli/cli/archive/v2.22.0/cli-2.22.0.tar.gz
Source0  : https://github.com/cli/cli/archive/v2.22.0/cli-2.22.0.tar.gz
Source1  : http://localhost/cgit/projects/gh-vendor/snapshot/gh-vendor-2.22.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause ISC MIT MPL-2.0 MPL-2.0-no-copyleft-exception Unlicense
Requires: gh-bin = %{version}-%{release}
Requires: gh-license = %{version}-%{release}
Requires: gh-man = %{version}-%{release}
BuildRequires : buildreq-golang
Patch1: 0001-Find-version-from-folder-name.patch

%description
# GitHub CLI
`gh` is GitHub on the command line. It brings pull requests, issues, and other GitHub concepts to the terminal next to where you are already working with `git` and your code.

%package bin
Summary: bin components for the gh package.
Group: Binaries
Requires: gh-license = %{version}-%{release}

%description bin
bin components for the gh package.


%package license
Summary: license components for the gh package.
Group: Default

%description license
license components for the gh package.


%package man
Summary: man components for the gh package.
Group: Default

%description man
man components for the gh package.


%prep
%setup -q -n cli-2.22.0
cd %{_builddir}
tar xf %{_sourcedir}/gh-vendor-2.22.0.tar.xz
cd %{_builddir}/cli-2.22.0
mkdir -p ./
cp -r %{_builddir}/gh-vendor-2.22.0/* %{_builddir}/cli-2.22.0/./
%patch1 -p1

%build
## build_prepend content
rm -f GNUmakefile
unset CLEAR_DEBUG_TERSE
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677172857
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1677172857
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gh
cp %{_builddir}/cli-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/gh/c89ceae9238469480d36c55e64715ab4ebaf345d || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/AlecAivazis/survey/v2/LICENSE %{buildroot}/usr/share/package-licenses/gh/c712a6f5c083360e03f0be6be5e883c1b8438984 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/AlecAivazis/survey/v2/terminal/LICENSE.txt %{buildroot}/usr/share/package-licenses/gh/7f45f6163bb54449d503978cff7537f6a468f1b1 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/MakeNowJust/heredoc/LICENSE %{buildroot}/usr/share/package-licenses/gh/7183d4b659f4d478e0e28019b20e039ef82bf47f || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/alecthomas/chroma/COPYING %{buildroot}/usr/share/package-licenses/gh/820a47085e1f88859859d16b894bc93b47683498 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/aymerick/douceur/LICENSE %{buildroot}/usr/share/package-licenses/gh/fad5441a68d1fdad917da8e6d409aa7eda4c9256 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/briandowns/spinner/LICENSE %{buildroot}/usr/share/package-licenses/gh/ab493383353f91b9ccc38085a5044fbef904b58b || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cenkalti/backoff/v4/LICENSE %{buildroot}/usr/share/package-licenses/gh/101c182fa18fd56a09164278f17e4282264c5e9e || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/charmbracelet/glamour/LICENSE %{buildroot}/usr/share/package-licenses/gh/73f98a7e55d7822f1f8cd5a630396d2b55cf61a2 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/charmbracelet/lipgloss/LICENSE %{buildroot}/usr/share/package-licenses/gh/463b4773c5faf583f0fd86647753e1bdc2a9a2a7 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cli/browser/LICENSE %{buildroot}/usr/share/package-licenses/gh/64a8107cababd5ee8cf663dd2188c0ff921fff0e || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cli/go-gh/LICENSE %{buildroot}/usr/share/package-licenses/gh/5c0e418ff5750461e481972fdc40ecb88ce84b26 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cli/oauth/LICENSE %{buildroot}/usr/share/package-licenses/gh/01ca397f4abd164e123dc5074faab85a793d2be4 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cli/safeexec/LICENSE %{buildroot}/usr/share/package-licenses/gh/be69f2983ddf5f5d0158292a8730a1ee8572cbe5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cli/shurcooL-graphql/LICENSE %{buildroot}/usr/share/package-licenses/gh/b26ed3e87f7325e769386027648abb751d3c0d78 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/gh/b7a606730713ac061594edab33cf941704b4a95c || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/creack/pty/LICENSE %{buildroot}/usr/share/package-licenses/gh/37a5e9e1835e9b179f9d7175f25c3349d47b76f8 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/gh/d2f340a01dd48b589a70f627cf7058c585a315e4 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/dlclark/regexp2/LICENSE %{buildroot}/usr/share/package-licenses/gh/91cd2d65a9945545fba9e4d03f279aff97470252 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/fatih/color/LICENSE.md %{buildroot}/usr/share/package-licenses/gh/563519fec7769aaec054ee06cb429f39f0fdab89 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/gabriel-vasile/mimetype/LICENSE %{buildroot}/usr/share/package-licenses/gh/4a06de85fbb53323c0ed1925df9bbff1bfecf459 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/gdamore/encoding/LICENSE %{buildroot}/usr/share/package-licenses/gh/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/gdamore/tcell/v2/LICENSE %{buildroot}/usr/share/package-licenses/gh/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/gh/aa9b240f558caed367795f667629ccbca28f20b2 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/gh/7080652cc78cd9855d39e324529a3b5f3745dcd6 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/google/shlex/COPYING %{buildroot}/usr/share/package-licenses/gh/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/gorilla/css/LICENSE %{buildroot}/usr/share/package-licenses/gh/35198a9140fe1b6d87d173f55766aee0a171915e || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/gorilla/websocket/LICENSE %{buildroot}/usr/share/package-licenses/gh/307711a68aa375a23d90191db6f720426cf88402 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/package-licenses/gh/523489384296f403da31edf8edf6f9023d328517 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/package-licenses/gh/2ebe302ef4d8d257ac6f0a916285b51937a25641 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/hashicorp/go-version/LICENSE %{buildroot}/usr/share/package-licenses/gh/523489384296f403da31edf8edf6f9023d328517 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/henvic/httpretty/LICENSE.md %{buildroot}/usr/share/package-licenses/gh/574250c89dcd08b28faa1a2bfaf416a8b2922f18 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/gh/62446e71c226403f1a2e67d0f66ede03e3fbdd2f || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/itchyny/gojq/LICENSE %{buildroot}/usr/share/package-licenses/gh/e778e8bf017bd832b574f8e7f7eccaa9d6696bed || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/itchyny/timefmt-go/LICENSE %{buildroot}/usr/share/package-licenses/gh/71628ab3605a8d820ef218f1ba46f337874e3485 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/joho/godotenv/LICENCE %{buildroot}/usr/share/package-licenses/gh/0df3aedcaa5019ef639d23e9762bd199e0c9d109 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/kballard/go-shellquote/LICENSE %{buildroot}/usr/share/package-licenses/gh/3afc456546a3fa3e82c0d21844cd9911d7d4464b || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/lucasb-eyer/go-colorful/LICENSE %{buildroot}/usr/share/package-licenses/gh/3db0b48008abcd20f9be0bf8d2deb8cae2e98aa7 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/mattn/go-colorable/LICENSE %{buildroot}/usr/share/package-licenses/gh/5ca808f075931c5322193d4afd5a3370c824f810 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/mattn/go-isatty/LICENSE %{buildroot}/usr/share/package-licenses/gh/5b53018d7f0706e49275a92d36b54cfbfbb71367 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/gh/5ca808f075931c5322193d4afd5a3370c824f810 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/mgutz/ansi/LICENSE %{buildroot}/usr/share/package-licenses/gh/69bd14555bdab2001efa07a655af9def7438e017 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/microcosm-cc/bluemonday/LICENSE.md %{buildroot}/usr/share/package-licenses/gh/02888e94069ac505326853d0d7ec0b1a968c5fb2 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/muesli/reflow/LICENSE %{buildroot}/usr/share/package-licenses/gh/0b85499b6fbedc267bcf411145ec8a8e8c2e8cba || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/muesli/termenv/LICENSE %{buildroot}/usr/share/package-licenses/gh/0b85499b6fbedc267bcf411145ec8a8e8c2e8cba || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/muhammadmuzzammil1998/jsonc/LICENSE %{buildroot}/usr/share/package-licenses/gh/821e43b51399949065cc2359cf257a19e0805157 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/olekukonko/tablewriter/LICENSE.md %{buildroot}/usr/share/package-licenses/gh/7c15369a8295c6d2cd26b41618f5ba81e7e06eca || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/opentracing/opentracing-go/LICENSE %{buildroot}/usr/share/package-licenses/gh/9277f25d2ab38e908276aff21eb9ec917583277a || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/gh/cd3e4d932cee20da681e6b3bee8139cb4f734034 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/rivo/tview/LICENSE.txt %{buildroot}/usr/share/package-licenses/gh/eedc9b72f84e8706c540f5fba9edc046df7e9c05 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/rivo/uniseg/LICENSE.txt %{buildroot}/usr/share/package-licenses/gh/f60d047cd34de4c91b3a045ebf117fe54b3c279e || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/gh/da34754c05d40ff81f91de8c1b85ea6e5503e21d || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/shurcooL/githubv4/LICENSE %{buildroot}/usr/share/package-licenses/gh/b26ed3e87f7325e769386027648abb751d3c0d78 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/shurcooL/graphql/LICENSE %{buildroot}/usr/share/package-licenses/gh/b26ed3e87f7325e769386027648abb751d3c0d78 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/sourcegraph/jsonrpc2/LICENSE %{buildroot}/usr/share/package-licenses/gh/df31a06417c9774b3f8de44526422aa4a8e33532 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/gh/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/gh/b3c86ae465b21f7323059db335158b48187731c7 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/stretchr/objx/LICENSE %{buildroot}/usr/share/package-licenses/gh/9d0e87d9ac5974470fc21c575854718e8b6516be || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/gh/892204393ca075d09c8b1c1d880aba1ae0a2b805 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/thlib/go-timezone-local/LICENSE %{buildroot}/usr/share/package-licenses/gh/6d842099530d126dea37db858a755e444f4de3f7 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/yuin/goldmark-emoji/LICENSE %{buildroot}/usr/share/package-licenses/gh/d20b3c2e56d2e06baf41122c5b0b6dd0ca76c09d || :
cp %{_builddir}/gh-vendor-%{version}/vendor/github.com/yuin/goldmark/LICENSE %{buildroot}/usr/share/package-licenses/gh/efbb6e2284183e25da23cf92f883857f5c239128 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/golang.org/x/term/LICENSE %{buildroot}/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/gh/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/gh/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/gh-vendor-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/gh/74850a25a5319bdddc0d998eb8926c18bada282b || :
cp %{_builddir}/gh-vendor-%{version}/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/gh/b74b3b31bc15ad5e94fc1947d682aa3d84132fce || :
cp %{_builddir}/gh-vendor-%{version}/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/gh/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gh/01ca397f4abd164e123dc5074faab85a793d2be4
/usr/share/package-licenses/gh/02888e94069ac505326853d0d7ec0b1a968c5fb2
/usr/share/package-licenses/gh/0b85499b6fbedc267bcf411145ec8a8e8c2e8cba
/usr/share/package-licenses/gh/0df3aedcaa5019ef639d23e9762bd199e0c9d109
/usr/share/package-licenses/gh/101c182fa18fd56a09164278f17e4282264c5e9e
/usr/share/package-licenses/gh/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/gh/2ebe302ef4d8d257ac6f0a916285b51937a25641
/usr/share/package-licenses/gh/307711a68aa375a23d90191db6f720426cf88402
/usr/share/package-licenses/gh/35198a9140fe1b6d87d173f55766aee0a171915e
/usr/share/package-licenses/gh/37a5e9e1835e9b179f9d7175f25c3349d47b76f8
/usr/share/package-licenses/gh/3afc456546a3fa3e82c0d21844cd9911d7d4464b
/usr/share/package-licenses/gh/3db0b48008abcd20f9be0bf8d2deb8cae2e98aa7
/usr/share/package-licenses/gh/463b4773c5faf583f0fd86647753e1bdc2a9a2a7
/usr/share/package-licenses/gh/4a06de85fbb53323c0ed1925df9bbff1bfecf459
/usr/share/package-licenses/gh/523489384296f403da31edf8edf6f9023d328517
/usr/share/package-licenses/gh/563519fec7769aaec054ee06cb429f39f0fdab89
/usr/share/package-licenses/gh/574250c89dcd08b28faa1a2bfaf416a8b2922f18
/usr/share/package-licenses/gh/5b53018d7f0706e49275a92d36b54cfbfbb71367
/usr/share/package-licenses/gh/5c0e418ff5750461e481972fdc40ecb88ce84b26
/usr/share/package-licenses/gh/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/gh/62446e71c226403f1a2e67d0f66ede03e3fbdd2f
/usr/share/package-licenses/gh/64a8107cababd5ee8cf663dd2188c0ff921fff0e
/usr/share/package-licenses/gh/69bd14555bdab2001efa07a655af9def7438e017
/usr/share/package-licenses/gh/6d842099530d126dea37db858a755e444f4de3f7
/usr/share/package-licenses/gh/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/gh/71628ab3605a8d820ef218f1ba46f337874e3485
/usr/share/package-licenses/gh/7183d4b659f4d478e0e28019b20e039ef82bf47f
/usr/share/package-licenses/gh/73f98a7e55d7822f1f8cd5a630396d2b55cf61a2
/usr/share/package-licenses/gh/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/gh/7c15369a8295c6d2cd26b41618f5ba81e7e06eca
/usr/share/package-licenses/gh/7f45f6163bb54449d503978cff7537f6a468f1b1
/usr/share/package-licenses/gh/820a47085e1f88859859d16b894bc93b47683498
/usr/share/package-licenses/gh/821e43b51399949065cc2359cf257a19e0805157
/usr/share/package-licenses/gh/892204393ca075d09c8b1c1d880aba1ae0a2b805
/usr/share/package-licenses/gh/91cd2d65a9945545fba9e4d03f279aff97470252
/usr/share/package-licenses/gh/9277f25d2ab38e908276aff21eb9ec917583277a
/usr/share/package-licenses/gh/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/gh/9d0e87d9ac5974470fc21c575854718e8b6516be
/usr/share/package-licenses/gh/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/gh/ab493383353f91b9ccc38085a5044fbef904b58b
/usr/share/package-licenses/gh/b26ed3e87f7325e769386027648abb751d3c0d78
/usr/share/package-licenses/gh/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/gh/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/gh/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/gh/be69f2983ddf5f5d0158292a8730a1ee8572cbe5
/usr/share/package-licenses/gh/c712a6f5c083360e03f0be6be5e883c1b8438984
/usr/share/package-licenses/gh/c7feacb4667f8c63c89e2eeeb9a913bd3ced8ac2
/usr/share/package-licenses/gh/c89ceae9238469480d36c55e64715ab4ebaf345d
/usr/share/package-licenses/gh/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/gh/d20b3c2e56d2e06baf41122c5b0b6dd0ca76c09d
/usr/share/package-licenses/gh/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/gh/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/gh/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/gh/df31a06417c9774b3f8de44526422aa4a8e33532
/usr/share/package-licenses/gh/e778e8bf017bd832b574f8e7f7eccaa9d6696bed
/usr/share/package-licenses/gh/eedc9b72f84e8706c540f5fba9edc046df7e9c05
/usr/share/package-licenses/gh/efbb6e2284183e25da23cf92f883857f5c239128
/usr/share/package-licenses/gh/f60d047cd34de4c91b3a045ebf117fe54b3c279e
/usr/share/package-licenses/gh/fad5441a68d1fdad917da8e6d409aa7eda4c9256

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gh-alias-delete.1
/usr/share/man/man1/gh-alias-list.1
/usr/share/man/man1/gh-alias-set.1
/usr/share/man/man1/gh-alias.1
/usr/share/man/man1/gh-api.1
/usr/share/man/man1/gh-auth-login.1
/usr/share/man/man1/gh-auth-logout.1
/usr/share/man/man1/gh-auth-refresh.1
/usr/share/man/man1/gh-auth-setup-git.1
/usr/share/man/man1/gh-auth-status.1
/usr/share/man/man1/gh-auth-token.1
/usr/share/man/man1/gh-auth.1
/usr/share/man/man1/gh-browse.1
/usr/share/man/man1/gh-codespace-code.1
/usr/share/man/man1/gh-codespace-cp.1
/usr/share/man/man1/gh-codespace-create.1
/usr/share/man/man1/gh-codespace-delete.1
/usr/share/man/man1/gh-codespace-edit.1
/usr/share/man/man1/gh-codespace-jupyter.1
/usr/share/man/man1/gh-codespace-list.1
/usr/share/man/man1/gh-codespace-logs.1
/usr/share/man/man1/gh-codespace-ports-forward.1
/usr/share/man/man1/gh-codespace-ports-visibility.1
/usr/share/man/man1/gh-codespace-ports.1
/usr/share/man/man1/gh-codespace-rebuild.1
/usr/share/man/man1/gh-codespace-ssh.1
/usr/share/man/man1/gh-codespace-stop.1
/usr/share/man/man1/gh-codespace.1
/usr/share/man/man1/gh-completion.1
/usr/share/man/man1/gh-config-get.1
/usr/share/man/man1/gh-config-list.1
/usr/share/man/man1/gh-config-set.1
/usr/share/man/man1/gh-config.1
/usr/share/man/man1/gh-extension-browse.1
/usr/share/man/man1/gh-extension-create.1
/usr/share/man/man1/gh-extension-exec.1
/usr/share/man/man1/gh-extension-install.1
/usr/share/man/man1/gh-extension-list.1
/usr/share/man/man1/gh-extension-remove.1
/usr/share/man/man1/gh-extension-search.1
/usr/share/man/man1/gh-extension-upgrade.1
/usr/share/man/man1/gh-extension.1
/usr/share/man/man1/gh-gist-clone.1
/usr/share/man/man1/gh-gist-create.1
/usr/share/man/man1/gh-gist-delete.1
/usr/share/man/man1/gh-gist-edit.1
/usr/share/man/man1/gh-gist-list.1
/usr/share/man/man1/gh-gist-view.1
/usr/share/man/man1/gh-gist.1
/usr/share/man/man1/gh-gpg-key-add.1
/usr/share/man/man1/gh-gpg-key-delete.1
/usr/share/man/man1/gh-gpg-key-list.1
/usr/share/man/man1/gh-gpg-key.1
/usr/share/man/man1/gh-issue-close.1
/usr/share/man/man1/gh-issue-comment.1
/usr/share/man/man1/gh-issue-create.1
/usr/share/man/man1/gh-issue-delete.1
/usr/share/man/man1/gh-issue-develop.1
/usr/share/man/man1/gh-issue-edit.1
/usr/share/man/man1/gh-issue-list.1
/usr/share/man/man1/gh-issue-lock.1
/usr/share/man/man1/gh-issue-pin.1
/usr/share/man/man1/gh-issue-reopen.1
/usr/share/man/man1/gh-issue-status.1
/usr/share/man/man1/gh-issue-transfer.1
/usr/share/man/man1/gh-issue-unlock.1
/usr/share/man/man1/gh-issue-unpin.1
/usr/share/man/man1/gh-issue-view.1
/usr/share/man/man1/gh-issue.1
/usr/share/man/man1/gh-label-clone.1
/usr/share/man/man1/gh-label-create.1
/usr/share/man/man1/gh-label-delete.1
/usr/share/man/man1/gh-label-edit.1
/usr/share/man/man1/gh-label-list.1
/usr/share/man/man1/gh-label.1
/usr/share/man/man1/gh-pr-checkout.1
/usr/share/man/man1/gh-pr-checks.1
/usr/share/man/man1/gh-pr-close.1
/usr/share/man/man1/gh-pr-comment.1
/usr/share/man/man1/gh-pr-create.1
/usr/share/man/man1/gh-pr-diff.1
/usr/share/man/man1/gh-pr-edit.1
/usr/share/man/man1/gh-pr-list.1
/usr/share/man/man1/gh-pr-lock.1
/usr/share/man/man1/gh-pr-merge.1
/usr/share/man/man1/gh-pr-ready.1
/usr/share/man/man1/gh-pr-reopen.1
/usr/share/man/man1/gh-pr-review.1
/usr/share/man/man1/gh-pr-status.1
/usr/share/man/man1/gh-pr-unlock.1
/usr/share/man/man1/gh-pr-view.1
/usr/share/man/man1/gh-pr.1
/usr/share/man/man1/gh-release-create.1
/usr/share/man/man1/gh-release-delete-asset.1
/usr/share/man/man1/gh-release-delete.1
/usr/share/man/man1/gh-release-download.1
/usr/share/man/man1/gh-release-edit.1
/usr/share/man/man1/gh-release-list.1
/usr/share/man/man1/gh-release-upload.1
/usr/share/man/man1/gh-release-view.1
/usr/share/man/man1/gh-release.1
/usr/share/man/man1/gh-repo-archive.1
/usr/share/man/man1/gh-repo-clone.1
/usr/share/man/man1/gh-repo-create.1
/usr/share/man/man1/gh-repo-delete.1
/usr/share/man/man1/gh-repo-deploy-key-add.1
/usr/share/man/man1/gh-repo-deploy-key-delete.1
/usr/share/man/man1/gh-repo-deploy-key-list.1
/usr/share/man/man1/gh-repo-deploy-key.1
/usr/share/man/man1/gh-repo-edit.1
/usr/share/man/man1/gh-repo-fork.1
/usr/share/man/man1/gh-repo-list.1
/usr/share/man/man1/gh-repo-rename.1
/usr/share/man/man1/gh-repo-set-default.1
/usr/share/man/man1/gh-repo-sync.1
/usr/share/man/man1/gh-repo-view.1
/usr/share/man/man1/gh-repo.1
/usr/share/man/man1/gh-run-cancel.1
/usr/share/man/man1/gh-run-download.1
/usr/share/man/man1/gh-run-list.1
/usr/share/man/man1/gh-run-rerun.1
/usr/share/man/man1/gh-run-view.1
/usr/share/man/man1/gh-run-watch.1
/usr/share/man/man1/gh-run.1
/usr/share/man/man1/gh-search-commits.1
/usr/share/man/man1/gh-search-issues.1
/usr/share/man/man1/gh-search-prs.1
/usr/share/man/man1/gh-search-repos.1
/usr/share/man/man1/gh-search.1
/usr/share/man/man1/gh-secret-delete.1
/usr/share/man/man1/gh-secret-list.1
/usr/share/man/man1/gh-secret-set.1
/usr/share/man/man1/gh-secret.1
/usr/share/man/man1/gh-ssh-key-add.1
/usr/share/man/man1/gh-ssh-key-delete.1
/usr/share/man/man1/gh-ssh-key-list.1
/usr/share/man/man1/gh-ssh-key.1
/usr/share/man/man1/gh-status.1
/usr/share/man/man1/gh-workflow-disable.1
/usr/share/man/man1/gh-workflow-enable.1
/usr/share/man/man1/gh-workflow-list.1
/usr/share/man/man1/gh-workflow-run.1
/usr/share/man/man1/gh-workflow-view.1
/usr/share/man/man1/gh-workflow.1
/usr/share/man/man1/gh.1
