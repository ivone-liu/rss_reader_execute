<?php

namespace app\api\common;

use think\Validate;
use think\facade\Cache;
use app\api\controller\Send;

class Common {

	use Send;

	/**
	* 验证参数
	*/
	public static function valid(Validate $obj) {
		if(!$obj->check(input(''))){
			return self::returnMsg(500,$obj->getError());
		}
	}

	/**
	* 中文字符分片
	*/
	public static function mb_str_split($str,$split_length=1,$charset="UTF-8"){
		if(func_num_args()==1){
		return preg_split('/(?<!^)(?!$)/u', $str);
		}
		if($split_length<1)return false;
		$len = mb_strlen($str, $charset);
		$arr = array();
		for($i=0;$i<$len;$i+=$split_length){
		$s = mb_substr($str, $i, $split_length, $charset);
		$arr[] = $s;
		}
		return $arr;
	}

}
	