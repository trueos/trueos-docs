# Created by: Kris Moore <kmoore@FreeBSD.org>
# $FreeBSD$

PORTNAME=	trueos-handbook
PORTVERSION=	%%CHGVERSION%%
CATEGORIES=	misc

MAINTAINER=	kmoore@FreeBSD.org
COMMENT=	TrueOS html handbook

LICENSE=	BSD3CLAUSE

BUILD_DEPENDS=	sphinx-build:textproc/py-sphinx \
		${PYTHON_PKGNAMEPREFIX}sphinx-intl>=0:textproc/py-sphinx-intl \
		${PYTHON_PKGNAMEPREFIX}sphinxcontrib-httpdomain>=0:textproc/py-sphinxcontrib-httpdomain \
		${PYTHON_PKGNAMEPREFIX}sphinx_rtd_theme>=0:textproc/py-sphinx_rtd_theme \
		${PYTHON_PKGNAMEPREFIX}alabaster>=0:textproc/py-alabaster \
		${PYTHON_PKGNAMEPREFIX}sphinx_numfig>=r13:textproc/py-sphinx_numfig \
		${PYTHON_PKGNAMEPREFIX}sphinx_wikipedia>=0:textproc/py-sphinx_wikipedia 

USES=		python tar:xz
NO_BUILD=	yes

WRKSRC_SUBDIR=	trueos-handbook

USE_GITHUB=	yes
GH_ACCOUNT=	trueos
GH_PROJECT=	trueos-docs
GH_TAGNAME=	%%GHTAG%%

.include <bsd.port.options.mk>

do-install:
	@cd ${WRKSRC} && make html
	${MKDIR} ${STAGEDIR}${PREFIX}/share/trueos
	@cp -r ${WRKSRC}/_build/html ${STAGEDIR}${PREFIX}/share/trueos/handbook

.include <bsd.port.mk>
