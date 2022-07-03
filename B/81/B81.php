<?php
/**
 * Get 1 Line from STDIN
 *
 * @method get()
 * @return
 *   - string or FALSE
 */
class Stdin {
    static function get() {
        if ($result = fgets(STDIN)) {
            $result = trim($result);
            return $result;
        }
        return FALSE;
    }
}

/** 
 * Get Multi Line from STDIN
 *
 * @method get()
 * @param int $max_num: 最大取得可能行
 * @return
 *   - array()
 */
class Stdins {
    static function get($max_num) {
        $list = array();
        for ($i=0; $i < $max_num; $i++) {
            $result = Stdin::get();
            if ($result == FALSE) {
                break;
            } else {
                array_push($list, $result);
            }
        }
        return $list;
    }
}

/**
 * Get 1 Line from File
 *
 * @method get()
 * @return
 *   - string or FALSE
 */
class GetLineFromFile {
    static function get($filename) {
        $fp = fopen($filename, 'r');
        if ($result = fgets($fp)) {
            $result = trim($result);
            return $result;
        }
        return FALSE;
    }
}

/** 
 * Get Multi Line from File
 *
 * @method get()
 * @param int $filename: ファイル名
 * @param int $max_num: 最大取得可能行
 * @return
 *   - array()
 */
class GetLinesFromFile {
    static function get($filename, $max_num) {
        $list = array();
        for ($i=0; $i < $max_num; $i++) {
            $result = GetLineFromfile::get($filename);
            if ($result == FALSE) {
                break;
            } else {
                array_push($list, $result);
            }
        }
        return $list;
    }
}

/**
 * Set Data of Paiza-format to Array
 *
 * @method setData()
 * @method getData()
 * @param int $max_num
 */
class PaizaData {
    function __construct() {
        $this->data = array();
    }
    function setData($data) {
        $this->data[] = $data;
    }
    function getData($array_num) {
        return $this->data[($array_num-1)];
    }
}

/**
 * 判定した数値を返す
 */
class CountScore {
    public $SCORE = 0;
    function judge($current_data, $before_data=null, $before_line_data=null, $after_line_data=null) {
        $this->current_data = $current_data;
        $this->before_data = $before_data;
        $this->before_line_data = $before_line_data;
    }
}

/**
 *  main
 */
$paiza = new PaizaData();
list($tate_max, $yoko_max) = explode(' ', trim(Stdin::get(1))); // parse First Line
$paiza->setData(Stdins::get($tate_max)); // set Second Data
print_r($paiza->data);

$split_data = array(); // コンテンツデータを１文字ずつ分離して格納する
for ($i=2; $i <= $tate_max; $i++) {
    $split_data[] = str_split($paiza->getData($i));
    print_r($split_data);
}

/**
 * データ分析開始
 * 条件
 * 全ての行で判定する 
 * 前がなしで次が. 0
 * 前がなしで次が# +1
 * 前が.で次が# +1
 * 前が.で次が. 0
 * 前が#で次が# 0
 * 前が#で次が. +1
 * -- 最初の行と最後の行は判定する
 * 最初/最終行.なら 0
 * 最初/最終行#なら +1
 * -- 最初の行以外は判定する
 * 前の行がなしで.0
 * 前の行がなしで# +1
 * 前の行が.で. 0
 * 前の行が#で. +1
 * 前の行が.で# +1
 * 前の行が#で # 0
 * --判定条件終了 --
 */
// .##.
// .##.
// .##.
// .##.
// 0211 4
// 0101 2
// 0101 2
// 0211 4
//=12

// ..#.
// ..#.
// ###.
// ..#.
// 0021
// 0011
// 2101
// 1121
// =14
?>
