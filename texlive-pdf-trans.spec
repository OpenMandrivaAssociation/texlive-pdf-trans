Name:		texlive-pdf-trans
Version:	32809
Release:	2
Summary:	A set of macros for various transformations of TeX boxes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/pdf-trans
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf-trans.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf-trans.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pdf-trans is a set of macros offering various transformations
of TeX boxes (based on plain and pdfeTeX primitives). It was
initially inspired by trans.tex, remade to work with pdfTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pdf-trans/pdf-trans.tex
%doc %{_texmfdistdir}/doc/generic/pdf-trans/example.pdf
%doc %{_texmfdistdir}/doc/generic/pdf-trans/example.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
