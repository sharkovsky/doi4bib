from . import import_dois

__all__ = ['add_dois_to_bib']

def add_dois_to_bib(bib_db, logger=None):
    """Enriches a bib database with DOI references.

    DOI references are obtained by contacting the crossref API.

    Args:
        bib_db: a bib databse in the format specified by biblib.
        logger: logger instance
    """

    for key, entry in bib_db.items():

        title = entry['title']
        logger.debug(key + ' ' + title)

        if 'doi' in entry.keys():
            if logger is not None:
                logger.debug(key + ' skipped because doi entry already present.')
        else:
            ret = import_dois.crossref_query_title(title)
            retries = 0
            while not ret['success'] and retries < import_dois.MAX_RETRIES_ON_ERROR:
                retries += 1
                logger.debug(key + ' retry: ' + str(retries))
                ret = import_dois.crossref_query_title(title)

            if retries < import_dois.MAX_RETRIES_ON_ERROR:
                result = ret["result"]

                if result["similarity"] >= 0.8:
                    entry.update(doi=result['doi'])

                    if logger is not None:
                        logger.debug(key + ' matched with similarity: ' + str(result["similarity"]))
                else:
                    if logger is not None:
                        logger.debug(key + ' failed match with ' + result['crossref_title'] + ' similarity: ' + str(result["similarity"]))
            else:
                if logger is not None:
                    logger.info(key + ' reached maximum number of retries contacting CrossRef API.')

    return bib_db


