%global tl_name pdf-trans
%global tl_revision 32809

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	A set of macros for various transformations of TeX boxes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/pdf-trans
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf-trans.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdf-trans.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
pdf-trans is a set of macros offering various transformations of TeX
boxes (based on plain and pdfeTeX primitives). It was initially inspired
by trans.tex, remade to work with pdfTeX.

