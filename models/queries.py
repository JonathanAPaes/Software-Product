class MyQueries:

    # Selects
    SELECT_ULTIMO_APONTAMENTO = """
    SELECT
        A.DATA_APONTAMENTO,
        A.HORA_APONTAMENTO,
        A.HOME_OFFICE, 
        A.ENTRADA_FLEXIVEL,
        A.ALMOCO_FLEXIVEL, 
        A.HORA_EXTRA,
        CASE WHEN A.CONTADOR % 2 = 1 THEN 'LIGADO' ELSE 'DESLIGADO' END AS ESTADO
    FROM
        APONTAMENTOS A
    ORDER BY
        A.DATA_APONTAMENTO DESC,
        A.HORA_APONTAMENTO DESC
    LIMIT 1;    
    """
    
    SELECT_FUNCIONARIO = """
    SELECT
        C.NOME AS EMPRESA_NOME,
        F.NOME AS FUNCIONARIO_NOME,
        A.CONTADOR,
        CASE WHEN A.CONTADOR % 2 = 1 THEN 'LIGADO' ELSE 'DESLIGADO' END AS ESTADO,
        A.DATA_APONTAMENTO,
        A.HORA_APONTAMENTO,
        A.LATITUDE,
        A.LONGITUDE,
        A.DESCRICAO
    FROM
        APONTAMENTOS A
    JOIN
        EMPRESAS C ON A.ID_EMPRESA = C.ID
    JOIN
        FUNCIONARIOS F ON A.ID_FUNCIONARIO = F.ID;

    """
    
    # Inserts
    INSERT_APONTAMENTOS = """
    INSERT INTO APONTAMENTOS (
        ID_EMPRESA, 
        ID_FUNCIONARIO, 
        ID_EVENTO,
        DATA_APONTAMENTO, 
        HORA_APONTAMENTO,  
        LATITUDE, 
        LONGITUDE,
        USER_AGENT,
        DESCRICAO
    )
    VALUES (%s, %s, %s, CURDATE(), CURTIME(), %s, %s, %s, %s);
    
    """
    
    # Inserts
    API_INSERT_APONTAMENTOS = """
    INSERT INTO APONTAMENTOS (
        ID_EMPRESA, 
        ID_FUNCIONARIO, 
        ID_EVENTO,
        DATA_APONTAMENTO, 
        HORA_APONTAMENTO,  
        LATITUDE, 
        LONGITUDE,
        USER_AGENT,
        DESCRICAO
    )
    VALUES (%s, %s, %s, CURDATE(), CURTIME(), %s, %s, %s, %s);
    
    """
