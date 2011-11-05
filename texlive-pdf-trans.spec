# revision 15878
# category Package
# catalog-ctan /macros/generic/pdf-trans
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license pd
# catalog-version 2.2
Name:		texlive-pdf-trans
Version:	2.2
Release:	1
Summary:	A set of macros for various transformations of TeX boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/pdf-trans
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf-trans.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf-trans.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
pdf-trans is a set of macros for various transformations of TeX
boxes (based on plain and pdfeTeX primitives). It was initially
inspired by trans.tex, remade to work with pdfTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pdf-trans/pdf-trans.tex
%doc %{_texmfdistdir}/doc/generic/pdf-trans/example.pdf
%doc %{_texmfdistdir}/doc/generic/pdf-trans/example.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
