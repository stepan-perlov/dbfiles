CREATE OR REPLACE FUNCTION test.function2() RETURNS void AS
$body$
BEGIN
    PERFORM 1 FROM test.table2;
END;
$body$ LANGUAGE plpgsql STABLE SECURITY DEFINER;
