
--CREATE TABLE [dbo].[NM_MEDICAID_DATA](
--[record] [nvarchar](max) NOT NULL
--);


CREATE TABLE dbo.NM_MEDICAID_DATA (

[""] nvarchar(max),
["record"] nvarchar(max),
["uuid"] nvarchar(max),
["date"] nvarchar(max),
["markers"] nvarchar(max),
["status"] nvarchar(max),
["s2"] nvarchar(max),
["s3"] nvarchar(max),
["s4"] nvarchar(max),
["s5"] nvarchar(max),

);


--DECLARE @data_file_path AS nvarchar(max) = 'C:\Users\css7c\OneDrive\Desktop\NM_DATA\nm_sample_data.csv'
--DECLARE @sql VARCHAR(MAX)


BULK INSERT dbo.NM_MEDICAID_DATA
FROM 'C:\Users\css7c\OneDrive\Desktop\NM_DATA\TEST.csv'
WITH
(
  FIELDTERMINATOR = ',',
  ROWTERMINATOR = '\n',
  ROWS_PER_BATCH = 10000, 
  FIRSTROW = 2, --IF THE FIRST ROW IS A COLUMN HEADER, THEN USE 2
  TABLOCK
)

SELECT COUNT(*) FROM dbo.NM_MEDICAID_DATA;
SELECT * FROM NM_MEDICAID_DATA



/*ALTER TABLE NM_MEDICAID_DATA REBUILD; */

/*

SET @sql = '
BULK INSERT dbo.NM_Medicaid
FROM ''' + @data_file_path + '''
WITH
(
	FORMAT=''CSV'',
	FIRSTROW = 2,
	FIELDTERMINATOR = '','',
	ROWTERMINATOR = ''\n''
)
'

EXEC(@sql)
GO

*/