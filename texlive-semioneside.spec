Name:		texlive-semioneside
Version:	15878
Release:	2
Summary:	Put only special contents on left-hand pages in two sided layout
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/semioneside
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semioneside.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semioneside.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semioneside.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package supports the preparation of semi one sided
documents. That is, two sided documents, where all text is
output on right-hand pages--as in a one-sided documents--and
only special contents are output on left-hand pages on user
request, e.g., floating objects.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/semioneside/semioneside.sty
%doc %{_texmfdistdir}/doc/latex/semioneside/README
%doc %{_texmfdistdir}/doc/latex/semioneside/example.tex
%doc %{_texmfdistdir}/doc/latex/semioneside/figure.mp
%doc %{_texmfdistdir}/doc/latex/semioneside/semioneside.pdf
#- source
%doc %{_texmfdistdir}/source/latex/semioneside/semioneside.dtx
%doc %{_texmfdistdir}/source/latex/semioneside/semioneside.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
