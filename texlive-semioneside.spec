# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/semioneside
# catalog-date 2007-02-26 21:24:31 +0100
# catalog-license lppl
# catalog-version v0.41
Name:		texlive-semioneside
Version:	v0.41
Release:	2
Summary:	Put only special contents on left-hand pages in two sided layout
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/semioneside
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semioneside.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semioneside.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/semioneside.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.41-2
+ Revision: 755907
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.41-1
+ Revision: 719505
- texlive-semioneside
- texlive-semioneside
- texlive-semioneside
- texlive-semioneside

