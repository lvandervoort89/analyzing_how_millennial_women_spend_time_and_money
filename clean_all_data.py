'''
This script cleans the metadata dataframe and the text datatframe.
'''

import re
import string

import pandas as pd

# helper function to remove blanks rows
def remove_blank_rows(diarist_df):
    '''
    A function that removes blanks rows in the dataframe.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where blank rows for age and location have
    been dropped.
    '''
    diarist_df = diarist_df[diarist_df.age != 'BLANK']
    diarist_df = diarist_df[diarist_df.location != 'BLANK']

    return diarist_df

# create function to clean salaries by removing common characters in salaries
def clean_salaries_round_1(text):
    '''
    Removes $ , from text.

    Parameters
    ----------
    text : A string of uncleaned text.

    Returns
    -------
    The original text that has been cleaned with $ and , removed.
    '''
    text = text.replace('$', '')
    text = text.replace(',', '')

    return text

def clean_salaries_round_2(diarist_df):
    '''
    A function that manually fix salaries that aren't just 1 number. Takes
    current salary (no bonuses). If unemployed, put 0. If salary range given,
    takes average. If hourly rate, calculated per year based on 40 hours/week.
    If daily rate given, calculated per year based on 5 days/week
    and 52 weeks per year.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where specific diarists salaries with errors
    have been cleaned.
    '''
    diarist_df.at[0, 'salary'] = 187000
    diarist_df.at[2, 'salary'] = 0
    diarist_df.at[3, 'salary'] = 145500
    diarist_df.at[10, 'salary'] = 325000
    diarist_df.at[11, 'salary'] = 128000
    diarist_df.at[12, 'salary'] = 103500
    diarist_df.at[13, 'salary'] = 190000
    diarist_df.at[15, 'salary'] = 0
    diarist_df.at[26, 'salary'] = 105000
    diarist_df.at[27, 'salary'] = 230961
    diarist_df.at[28, 'salary'] = 91000
    diarist_df.at[30, 'salary'] = 40000
    diarist_df.at[31, 'salary'] = 78600
    diarist_df.at[33, 'salary'] = 45500
    diarist_df.at[36, 'salary'] = 0
    diarist_df.at[41, 'salary'] = 96000
    diarist_df.at[42, 'salary'] = 100000
    diarist_df.at[44, 'salary'] = 105000
    diarist_df.at[45, 'salary'] = 27246
    diarist_df.at[47, 'salary'] = 43680
    diarist_df.at[48, 'salary'] = 50000
    diarist_df.at[56, 'salary'] = 50000
    diarist_df.at[57, 'salary'] = 80000
    diarist_df.at[58, 'salary'] = 0
    diarist_df.at[68, 'salary'] = 44100
    diarist_df.at[69, 'salary'] = 66000
    diarist_df.at[71, 'salary'] = 71000
    diarist_df.at[77, 'salary'] = 60000
    diarist_df.at[79, 'salary'] = 28000
    diarist_df.at[85, 'salary'] = 0
    diarist_df.at[86, 'salary'] = 34840
    diarist_df.at[87, 'salary'] = 83000
    diarist_df.at[88, 'salary'] = 76500
    diarist_df.at[90, 'salary'] = 86500
    diarist_df.at[93, 'salary'] = 115000
    diarist_df.at[94, 'salary'] = 37440
    diarist_df.at[95, 'salary'] = 32000
    diarist_df.at[96, 'salary'] = 150000
    diarist_df.at[97, 'salary'] = 76000
    diarist_df.at[99, 'salary'] = 120000
    diarist_df.at[101, 'salary'] = 50000
    diarist_df.at[102, 'salary'] = 70000
    diarist_df.at[112, 'salary'] = 115000
    diarist_df.at[114, 'salary'] = 62473
    diarist_df.at[116, 'salary'] = 110000
    diarist_df.at[119, 'salary'] = 240000
    diarist_df.at[120, 'salary'] = 104738
    diarist_df.at[121, 'salary'] = 0
    diarist_df.at[125, 'salary'] = 40000

    return diarist_df

def clean_salaries_round_3(diarist_df):
    '''
    A function that manually fix salaries that aren't just 1 number. Takes
    current salary (no bonuses). If unemployed, put 0. If salary range given,
    takes average. If hourly rate, calculated per year based on 40 hours/week.
    If daily rate given, calculated per year based on 5 days/week
    and 52 weeks per year.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where specific diarists salaries with errors
    have been cleaned.
    '''
    diarist_df.at[126, 'salary'] = 60000
    diarist_df.at[127, 'salary'] = 38264
    diarist_df.at[128, 'salary'] = 82000
    diarist_df.at[133, 'salary'] = 5000
    diarist_df.at[136, 'salary'] = 150000
    diarist_df.at[143, 'salary'] = 154000
    diarist_df.at[145, 'salary'] = 100000
    diarist_df.at[148, 'salary'] = 14856
    diarist_df.at[152, 'salary'] = 63500
    diarist_df.at[158, 'salary'] = 82500
    diarist_df.at[159, 'salary'] = 61948
    diarist_df.at[162, 'salary'] = 84300
    diarist_df.at[163, 'salary'] = 135000
    diarist_df.at[165, 'salary'] = 90000
    diarist_df.at[166, 'salary'] = 65000
    diarist_df.at[169, 'salary'] = 80000
    diarist_df.at[170, 'salary'] = 105000
    diarist_df.at[171, 'salary'] = 515000
    diarist_df.at[173, 'salary'] = 74000
    diarist_df.at[175, 'salary'] = 45000
    diarist_df.at[179, 'salary'] = 0
    diarist_df.at[180, 'salary'] = 73850
    diarist_df.at[186, 'salary'] = 31915
    diarist_df.at[187, 'salary'] = 52000
    diarist_df.at[190, 'salary'] = 108000
    diarist_df.at[192, 'salary'] = 137000
    diarist_df.at[193, 'salary'] = 89000
    diarist_df.at[194, 'salary'] = 55640
    diarist_df.at[198, 'salary'] = 111524
    diarist_df.at[201, 'salary'] = 144870
    diarist_df.at[202, 'salary'] = 210000
    diarist_df.at[204, 'salary'] = 104000
    diarist_df.at[205, 'salary'] = 80000
    diarist_df.at[209, 'salary'] = 45760
    diarist_df.at[213, 'salary'] = 180780
    diarist_df.at[214, 'salary'] = 72000
    diarist_df.at[215, 'salary'] = 133000
    diarist_df.at[217, 'salary'] = 30000
    diarist_df.at[219, 'salary'] = 77000
    diarist_df.at[221, 'salary'] = 36000
    diarist_df.at[223, 'salary'] = 61000
    diarist_df.at[224, 'salary'] = 52000
    diarist_df.at[228, 'salary'] = 115000
    diarist_df.at[229, 'salary'] = 145600
    diarist_df.at[232, 'salary'] = 280000
    diarist_df.at[238, 'salary'] = 46000
    diarist_df.at[242, 'salary'] = 20250
    diarist_df.at[248, 'salary'] = 39208
    diarist_df.at[249, 'salary'] = 43617

    return diarist_df

def clean_salaries_round_4(diarist_df):
    '''
    A function that manually fix salaries that aren't just 1 number. Takes
    current salary (no bonuses). If unemployed, put 0. If salary range given,
    takes average. If hourly rate, calculated per year based on 40 hours/week.
    If daily rate given, calculated per year based on 5 days/week
    and 52 weeks per year.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where specific diarists salaries with errors
    have been cleaned.
    '''
    diarist_df.at[251, 'salary'] = 44000
    diarist_df.at[259, 'salary'] = 120000
    diarist_df.at[260, 'salary'] = 40000
    diarist_df.at[261, 'salary'] = 20840
    diarist_df.at[262, 'salary'] = 59925
    diarist_df.at[264, 'salary'] = 149000
    diarist_df.at[272, 'salary'] = 285000
    diarist_df.at[274, 'salary'] = 42000
    diarist_df.at[276, 'salary'] = 96400
    diarist_df.at[277, 'salary'] = 170000
    diarist_df.at[280, 'salary'] = 62000
    diarist_df.at[284, 'salary'] = 64000
    diarist_df.at[287, 'salary'] = 100000
    diarist_df.at[292, 'salary'] = 180000
    diarist_df.at[297, 'salary'] = 52827
    diarist_df.at[298, 'salary'] = 85000
    diarist_df.at[299, 'salary'] = 208800
    diarist_df.at[300, 'salary'] = 200000
    diarist_df.at[301, 'salary'] = 125000
    diarist_df.at[302, 'salary'] = 34500
    diarist_df.at[304, 'salary'] = 70000
    diarist_df.at[307, 'salary'] = 70000
    diarist_df.at[308, 'salary'] = 37440
    diarist_df.at[311, 'salary'] = 52817
    diarist_df.at[312, 'salary'] = 122600
    diarist_df.at[315, 'salary'] = 51500
    diarist_df.at[328, 'salary'] = 120000
    diarist_df.at[329, 'salary'] = 92400
    diarist_df.at[330, 'salary'] = 50000
    diarist_df.at[331, 'salary'] = 155000
    diarist_df.at[332, 'salary'] = 33280
    diarist_df.at[333, 'salary'] = 41600
    diarist_df.at[344, 'salary'] = 49000
    diarist_df.at[346, 'salary'] = 26000
    diarist_df.at[347, 'salary'] = 94330
    diarist_df.at[348, 'salary'] = 23000
    diarist_df.at[349, 'salary'] = 100000
    diarist_df.at[350, 'salary'] = 35360
    diarist_df.at[355, 'salary'] = 26808
    diarist_df.at[357, 'salary'] = 78000
    diarist_df.at[358, 'salary'] = 52500
    diarist_df.at[359, 'salary'] = 30000
    diarist_df.at[360, 'salary'] = 150000
    diarist_df.at[364, 'salary'] = 52000
    diarist_df.at[366, 'salary'] = 56000
    diarist_df.at[367, 'salary'] = 167000
    diarist_df.at[371, 'salary'] = 72000
    diarist_df.at[377, 'salary'] = 75000
    diarist_df.at[384, 'salary'] = 15000

    return diarist_df

def clean_salaries_round_5(diarist_df):
    '''
    A function that manually fix salaries that aren't just 1 number. Takes
    current salary (no bonuses). If unemployed, put 0. If salary range given,
    takes average. If hourly rate, calculated per year based on 40 hours/week.
    If daily rate given, calculated per year based on 5 days/week
    and 52 weeks per year.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where specific diarists salaries with errors
    have been cleaned.
    '''
    diarist_df.at[387, 'salary'] = 110000
    diarist_df.at[390, 'salary'] = 34376
    diarist_df.at[392, 'salary'] = 115900
    diarist_df.at[397, 'salary'] = 57200
    diarist_df.at[408, 'salary'] = 194000
    diarist_df.at[414, 'salary'] = 200000
    diarist_df.at[417, 'salary'] = 120000
    diarist_df.at[424, 'salary'] = 54000
    diarist_df.at[426, 'salary'] = 34216
    diarist_df.at[432, 'salary'] = 48000
    diarist_df.at[439, 'salary'] = 80000
    diarist_df.at[444, 'salary'] = 45645
    diarist_df.at[450, 'salary'] = 20000
    diarist_df.at[452, 'salary'] = 120000
    diarist_df.at[456, 'salary'] = 21419
    diarist_df.at[457, 'salary'] = 125000
    diarist_df.at[461, 'salary'] = 85500
    diarist_df.at[481, 'salary'] = 30000
    diarist_df.at[487, 'salary'] = 500000
    diarist_df.at[490, 'salary'] = 32000
    diarist_df.at[495, 'salary'] = 104000
    diarist_df.at[499, 'salary'] = 115000

    return diarist_df

def clean_salaries_round_6(diarist_df):
    '''
    A function that manually fixes missing salaries by looking them up on the
    Refinery29 website.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where specific diarists salaries with errors
    have been cleaned by referencing the Refinery29 website.
    '''
    diarist_df.at[160, 'salary'] = 36255
    diarist_df.at[184, 'salary'] = 230000
    diarist_df.at[273, 'salary'] = 0
    diarist_df.at[338, 'salary'] = 37000
    diarist_df.at[339, 'salary'] = 65515
    diarist_df.at[356, 'salary'] = 128000
    diarist_df.at[361, 'salary'] = 11000
    diarist_df.at[389, 'salary'] = 123000
    diarist_df.at[406, 'salary'] = 92800
    diarist_df.at[415, 'salary'] = 85000
    diarist_df.at[421, 'salary'] = 48000
    diarist_df.at[422, 'salary'] = 55000
    diarist_df.at[428, 'salary'] = 31720
    diarist_df.at[433, 'salary'] = 44673
    diarist_df.at[434, 'salary'] = 62400
    diarist_df.at[436, 'salary'] = 86000
    diarist_df.at[448, 'salary'] = 56035
    diarist_df.at[455, 'salary'] = 10560
    diarist_df.at[458, 'salary'] = 12000
    diarist_df.at[469, 'salary'] = 61000
    diarist_df.at[485, 'salary'] = 60000
    diarist_df.at[494, 'salary'] = 44096
    diarist_df.at[498, 'salary'] = 16000

    return diarist_df

def clean_salaries_round_7(diarist_df):
    '''
    A function that converts the salary column to numeric, rounds the column,
    and drops any duplicate values.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where the salary column has been converted to
    a numeric type, rounded, and duplicate rows have been dropped.
    '''
    # convert salary column to numeric type
    diarist_df['salary'] = pd.to_numeric(diarist_df['salary'], errors='coerce')

    # Round salary column
    diarist_df.salary = diarist_df.salary.round()

    #Remove duplicates
    diarist_df.sort_values(['story_title', 'salary'], inplace=True, ascending=False)
    diarist_df.drop_duplicates(subset=['story_title', 'salary'], inplace=True)

    # Reset index
    diarist_df = diarist_df.reset_index(drop=True)

    return diarist_df

def clean_locations_round_1(diarist_df):
    '''
    A function that manually fixes the locations by fixing abbreviations and
    spelling.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df where specific diarists locations have been
    manually cleaned for spelling and mistakes.
    '''

    diarist_df.at[19, 'location'] = 'New York, NY'
    diarist_df.at[21, 'location'] = 'Los Angeles, CA'
    diarist_df.at[24, 'location'] = 'New York, NY'
    diarist_df.at[38, 'location'] = 'Boston, MA'
    diarist_df.at[62, 'location'] = 'Boston, MA'
    diarist_df.at[87, 'location'] = 'San Francisco, CA'
    diarist_df.at[107, 'location'] = 'New York, NY'
    diarist_df.at[108, 'location'] = 'San Francisco, CA'
    diarist_df.at[115, 'location'] = 'New York, NY'
    diarist_df.at[116, 'location'] = 'Philadelphia, PA'
    diarist_df.at[163, 'location'] = 'Baltimore, MD'
    diarist_df.at[235, 'location'] = 'Chicago, IL'
    diarist_df.at[243, 'location'] = 'Los Angeles, CA'
    diarist_df.at[250, 'location'] = 'New York, NY'
    diarist_df.at[258, 'location'] = 'New York, NY'
    diarist_df.at[310, 'location'] = 'Chicago, IL'
    diarist_df.at[330, 'location'] = 'Denver, CO'
    diarist_df.at[384, 'location'] = 'Chicago, IL'
    diarist_df.at[387, 'location'] = 'Chicago, IL'
    diarist_df.at[388, 'location'] = 'Chicago, IL'
    diarist_df.at[393, 'location'] = 'San Francisco, CA'
    diarist_df.at[405, 'location'] = 'Boston, MA'
    diarist_df.at[406, 'location'] = 'Boston, MA'
    diarist_df.at[422, 'location'] = 'Detroit, MI'
    diarist_df.at[429, 'location'] = 'New York, NY'
    diarist_df.at[55, 'location'] = 'Japan'
    diarist_df.at[273, 'location'] = 'Toronto'
    diarist_df.at[320, 'location'] = 'Bali, Indonesia'
    diarist_df.at[475, 'location'] = 'Chengdu, China'
    diarist_df.at[142, 'location'] = 'Canada'

    return diarist_df

def clean_locations_round_2(diarist_df):
    '''
    A function that adds a column if the diarist lives a nomadic lifestyle.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    An updated version of diarist_df in which a new column has been added and coded
    for diarists who live a nomadic lifestyle.
    '''
    diarist_df['nomad'] = 0
    diarist_df.at[96, 'nomad'] = 1
    diarist_df.at[171, 'nomad'] = 1
    diarist_df.at[298, 'nomad'] = 1
    diarist_df.at[431, 'nomad'] = 1
    diarist_df.at[472, 'nomad'] = 1

    return diarist_df

def clean_locations_round_3(diarist_df):
    '''
    A function that adds a column if the diarist lives internationally.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    An updated version of diarist_df in which a new column has been added and coded
    for diarists who live internationally.
    '''
    diarist_df['international'] = 0
    diarist_df.at[0, 'international'] = 1
    diarist_df.at[15, 'international'] = 1
    diarist_df.at[26, 'international'] = 1
    diarist_df.at[28, 'international'] = 1
    diarist_df.at[30, 'international'] = 1
    diarist_df.at[35, 'international'] = 1
    diarist_df.at[55, 'international'] = 1
    diarist_df.at[95, 'international'] = 1
    diarist_df.at[98, 'international'] = 1
    diarist_df.at[99, 'international'] = 1
    diarist_df.at[117, 'international'] = 1
    diarist_df.at[145, 'international'] = 1
    diarist_df.at[146, 'international'] = 1
    diarist_df.at[149, 'international'] = 1
    diarist_df.at[187, 'international'] = 1
    diarist_df.at[215, 'international'] = 1
    diarist_df.at[226, 'international'] = 1
    diarist_df.at[229, 'international'] = 1
    diarist_df.at[230, 'international'] = 1
    diarist_df.at[231, 'international'] = 1
    diarist_df.at[257, 'international'] = 1
    diarist_df.at[263, 'international'] = 1
    diarist_df.at[271, 'international'] = 1
    diarist_df.at[273, 'international'] = 1
    diarist_df.at[286, 'international'] = 1
    diarist_df.at[287, 'international'] = 1
    diarist_df.at[289, 'international'] = 1
    diarist_df.at[301, 'international'] = 1
    diarist_df.at[302, 'international'] = 1
    diarist_df.at[303, 'international'] = 1
    diarist_df.at[320, 'international'] = 1
    diarist_df.at[321, 'international'] = 1
    diarist_df.at[337, 'international'] = 1
    diarist_df.at[347, 'international'] = 1
    diarist_df.at[350, 'international'] = 1
    diarist_df.at[351, 'international'] = 1
    diarist_df.at[395, 'international'] = 1
    diarist_df.at[396, 'international'] = 1
    diarist_df.at[400, 'international'] = 1
    diarist_df.at[401, 'international'] = 1
    diarist_df.at[417, 'international'] = 1
    diarist_df.at[421, 'international'] = 1
    diarist_df.at[436, 'international'] = 1
    diarist_df.at[454, 'international'] = 1
    diarist_df.at[466, 'international'] = 1
    diarist_df.at[475, 'international'] = 1

    return diarist_df

def in_major_city(location):
    '''
    Takes in a location and returns a value of 0 or 1 if the input location is
    in one of the lists.

    Parameters
    ----------
    location : A text string of a location.

    Returns
    -------
    A new column coded with a 1 if the diarist lives in a major city in the lists
    below or a 0 if not.
    '''
    major_city_list_abbreviation = [
        'New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX',
        'Phoenix, AZ', 'Philadelphia, PA', 'San Antonio, TX', 'Dallas, TX',
        'San Jose, CA', 'Austin, TX', 'Jacksonville, FL', 'Fort Worth, TX',
        'Columbus, OH', 'Charlotte, NC', 'San Francisco, CA',
        'Indianapolis, IN', 'Seattle, WA', 'Denver, CO', 'Washington, DC',
        'Boston, MA', 'El Paso, TX', 'Nashville, TN', 'Detroit, MI',
        'Oklahoma City, OK'
        ]

    major_city_list_full_state = [
        'New York, New York', 'Los Angeles, California', 'Chicago, Illinois',
        'Houston, Texas', 'Phoenix, Arizona', 'Philadelphia, PA',
        'San Antonio, Texas', 'Dallas, Texas', 'San Jose, California',
        'Austin, Texas', 'Jacksonville, Florida', 'Fort Worth, Texas',
        'Columbus, Ohio', 'Charlotte, North Carolina',
        'San Francisco, California', 'Indianapolis, Indiana',
        'Seattle, Washington', 'Denver, Colorado', 'Washington DC',
        'Boston, Massachusetts', 'El Paso, Texas', 'Nashville, Tennessee',
        'Detroit, Michigan', 'Oklahoma City, Oklahoma'
        ]

    other_names_for_ny = ['Brooklyn, NY', 'Queens, NY', 'Manhattan, NY']

    if (
            location in major_city_list_abbreviation or
            location in major_city_list_full_state  or
            location in other_names_for_ny
        ):
        return 1
    return 0

def convert_age_to_int(diarist_df):
    '''
    A function that converts the age column to an integer.

    Parameters
    ----------
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    A cleaner version of diarist_df the age column has been converted to a
    numeric type.
    '''
    diarist_df.age = diarist_df.age.apply(int)

    return diarist_df

def clean_text_round_1(text_df, diarist_df):
    '''
    A function that converts text from a string to a list, removes unnecessary
    columns, and merges cleaned data together.

    Parameters
    ----------
    text_df: A dataframe containing only the text from the daily diaries.
    diarist_df : A dataframe containing only the metadata from the daily diaries.

    Returns
    -------
    An updated version of the dataframe named updated_text_df that has been cleaned
    and converted to a string.
    '''
    # Convert the diary text column from a list to a string
    text_df['diary_text_string'] = [', '.join(map(str, l)) for l in text_df['diary_text']]

    # Drop the diary_text as list column
    del text_df['diary_text']

    # Merge diarist_df with text_df
    updated_text_df = pd.merge(diarist_df, text_df, left_on='story_title', right_on='story_title')

    # Drop all columns but link and diary text from updated_text_df
    updated_text_df.drop(columns=[
        'age', 'salary', 'nomad', 'international', 'high_cost_of_living_area'],
                         inplace=True)

    return updated_text_df

def clean_text_round2(text):
    '''
    Make text lowercase, remove text in square brackets, remove punctuation,
    remove words containing numbers, remove additional punctuation and other
    non-sensical text.

    text: A string of text

    Returns
    -------
    A cleaned version of the text that makes it lowercase, removes text in square
    brackets, removes punctuation, removes words containing numbers, removes additional
    punctuation, and other non-sensical text.
    '''
    text = text.lower()
    text = re.sub('\\[.*?\\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(' — ', ' ', text)
    text = re.sub('\\w*\\d\\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('^', '', text)

    return text
